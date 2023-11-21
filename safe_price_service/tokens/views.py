from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import response, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from gnosis.eth.utils import fast_is_checksum_address

from . import serializers
from .clients import CannotGetPrice
from .services.price_service import get_price_service, is_chain_supported


class TokenPriceView(GenericAPIView):
    serializer_class = serializers.TokenPriceResponseSerializer
    lookup_field = "address"

    @method_decorator(cache_page(60 * 10))  # Cache 10 minutes
    def get(self, request, *args, **kwargs):
        chain_id = self.kwargs["chain_id"]
        address = self.kwargs["address"]

        if not is_chain_supported(chain_id):
            return response.Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data={
                    "code": 2,
                    "message": "Chain is not supported",
                    "arguments": [chain_id],
                },
            )

        if not fast_is_checksum_address(address):
            return response.Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data={
                    "code": 1,
                    "message": "Invalid ethereum address",
                    "arguments": [address],
                },
            )

        try:
            price_service = get_price_service(chain_id)
            data = {
                "fiat_code": "USD",
                "fiat_price": str(price_service.get_token_usd_price(address)),
                "timestamp": timezone.now(),  #FIXME
            }
            serializer = self.get_serializer(data=data)
            assert serializer.is_valid()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except CannotGetPrice:
            return Response(
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
                data={
                    "code": 10,
                    "message": "Price retrieval failed",
                    "arguments": [address],
                },
            )
