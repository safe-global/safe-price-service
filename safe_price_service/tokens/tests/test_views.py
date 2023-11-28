import logging
from unittest import mock
from unittest.mock import MagicMock

from django.urls import reverse
from django.utils import timezone

from eth_account import Account
from rest_framework import status
from rest_framework.test import APITestCase

from ..clients import CannotGetPrice
from ..services.price_service import PriceService

logger = logging.getLogger(__name__)


class TestTokenViews(APITestCase):
    ganache_chain_id = 1337

    @mock.patch.object(timezone, "now", return_value=timezone.now())
    def test_token_price_view(self, timezone_now_mock: MagicMock):
        chain_id = 1
        invalid_address = "0x1234"
        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    invalid_address,
                ),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.json(),
            {"arguments": [chain_id], "code": 2, "message": "Chain is not supported"},
        )

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    invalid_address,
                ),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.json(),
            {
                "arguments": [invalid_address],
                "code": 1,
                "message": "Invalid ethereum address",
            },
        )

        valid_address = Account.create().address
        with mock.patch.object(
            PriceService,
            "get_token_eth_value_from_oracles",
            return_value=4815,
            autospec=True,
        ) as get_token_eth_value_from_oracles_mock:
            with mock.patch.object(
                PriceService, "get_native_coin_usd_price", return_value=3, autospec=True
            ) as get_native_coin_usd_price_mock:
                response = self.client.get(
                    reverse(
                        "v1:tokens:price-usd",
                        args=(
                            chain_id,
                            valid_address,
                        ),
                    )
                )
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(
                    response.data,
                    {
                        "fiat_code": "USD",
                        "fiat_price": str(
                            get_token_eth_value_from_oracles_mock.return_value
                            * get_native_coin_usd_price_mock.return_value
                        ),
                        "timestamp": timezone_now_mock.return_value.isoformat().replace(
                            "+00:00", "Z"
                        ),
                    },
                )

    @mock.patch.object(
        PriceService, "get_native_coin_usd_price", return_value=321.2, autospec=True
    )
    def test_token_price_view_address_0(
        self, get_native_coin_usd_price_mock: MagicMock
    ):
        chain_id = 1
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    token_address,
                ),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.json(),
            {"arguments": [chain_id], "code": 2, "message": "Chain is not supported"},
        )

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    token_address,
                ),
            )
        )

        # Native token should be retrieved even if it is not part of the Token table
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["fiat_code"], "USD")
        self.assertEqual(response.data["fiat_price"], "321.2")
        self.assertTrue(response.data["timestamp"])

    @mock.patch.object(
        PriceService,
        "get_token_usd_price",
        side_effect=CannotGetPrice(),
    )
    def test_token_price_view_error(self, get_token_usd_price_mock: MagicMock):
        chain_id = 1
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    token_address,
                ),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(
            response.json(),
            {"arguments": [chain_id], "code": 2, "message": "Chain is not supported"},
        )

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse(
                "v1:tokens:price-usd",
                args=(
                    chain_id,
                    token_address,
                ),
            )
        )
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["message"], "Price retrieval failed")
        self.assertEqual(response.data["arguments"], [token_address])
