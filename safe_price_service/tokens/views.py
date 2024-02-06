from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import response, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from gnosis.eth.utils import fast_is_checksum_address

from safe_price_service import __version__

from . import serializers
from .clients import CannotGetPrice
from .services.price_service import (
    get_price_service,
    get_price_services,
    is_chain_supported,
)


class AboutView(GenericAPIView):
    """
    Returns information and configuration of the service
    """

    @method_decorator(cache_page(5 * 60))  # 5 minutes
    def get(self, request, format=None):
        chain_ids_configured = list(get_price_services().keys())
        content = {
            "name": "Safe Price Service",
            "version": __version__,
            "api_version": request.version,
            "secure": request.is_secure(),
            "host": request.get_host(),
            "headers": [x for x in request.META.keys() if "FORWARD" in x],
            "settings": {
                "CHAIN_IDS_CONFIGURED": chain_ids_configured,  # Don't reveal URLs
                "PRICES_CACHE_TTL_MINUTES": settings.PRICES_CACHE_TTL_MINUTES,
            },
        }
        return Response(content)


class TokenPriceView(GenericAPIView):
    serializer_class = serializers.TokenPriceResponseSerializer
    lookup_field = "address"

    @method_decorator(cache_page(60 * 10))  # Cache 10 minutes
    def get(self, request, *args, **kwargs):
        """
        Get token USD value for the given `chain_id` and ERC55 checksummed `address`.
        For the base currency of the network (for example, `Matic` for `Polygon network`)
        use `0x0000000000000000000000000000000000000000` as the token address
        """
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
            data = price_service.get_token_usd_price(address)
            serializer = self.get_serializer(data)
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
