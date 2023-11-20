import logging
from unittest import mock
from unittest.mock import MagicMock

from django.urls import reverse
from django.utils import timezone

from eth_account import Account
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase

from gnosis.safe.tests.safe_test_case import SafeTestCaseMixin

from ..clients import CannotGetPrice
from ..services import PriceService
from ..services.price_service import FiatCode, FiatPriceWithTimestamp

logger = logging.getLogger(__name__)


class TestTokenViews(APITestCase):
    chain_id = 1

    def test_token_price_view(self):
        invalid_address = "0x1234"
        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(self.chain_id, invalid_address,))
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)


    @mock.patch.object(
        PriceService, "get_native_coin_usd_price", return_value=321.2, autospec=True
    )
    def test_token_price_view_address_0(
        self, get_native_coin_usd_price_mock: MagicMock
    ):
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(self.chain_id, token_address,))
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
        token_address = "0x0000000000000000000000000000000000000000"

        response = self.client.get(
            reverse("v1:tokens:price-usd", args=(self.chain_id, token_address,))
        )

        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEqual(response.data["message"], "Price retrieval failed")
        self.assertEqual(response.data["arguments"], [token_address])
