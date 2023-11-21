import logging
from unittest import mock
from unittest.mock import MagicMock

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


from ..clients import CannotGetPrice
from ..services.price_service import PriceService

logger = logging.getLogger(__name__)


class TestTokenViews(APITestCase):
    ganache_chain_id = 1337

    def test_token_price_view(self):
        chain_id = 1
        invalid_address = "0x1234"
        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, invalid_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json(), {'arguments': [chain_id], 'code': 2, 'message': 'Chain is not supported'})

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, invalid_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json(),  {'arguments': [invalid_address], 'code': 1, 'message': 'Invalid ethereum address'})


    @mock.patch.object(
        PriceService, "get_native_coin_usd_price", return_value=321.2, autospec=True
    )
    def test_token_price_view_address_0(
        self, get_native_coin_usd_price_mock: MagicMock
    ):
        chain_id = 1
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, token_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json(), {'arguments': [chain_id], 'code': 2, 'message': 'Chain is not supported'})

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, token_address,))
        )

        # Native token should be retrieved even if it is not part of the Token table
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["fiat_code"], "USD")
        self.assertEqual(response.data["fiat_price"], "321.2")
        self.assertTrue(response.data["timestamp"])

    @mock.patch.object(
        PriceService,
        "get_native_coin_usd_price",
        side_effect=CannotGetPrice(),
    )
    def test_token_price_view_error(self, get_native_coin_usd_price_mock: MagicMock):
        chain_id = 1
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, token_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json(), {'arguments': [chain_id], 'code': 2, 'message': 'Chain is not supported'})

        chain_id = self.ganache_chain_id
        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(chain_id, token_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["message"], "Price retrieval failed")
        self.assertEqual(response.data["arguments"], [token_address])
