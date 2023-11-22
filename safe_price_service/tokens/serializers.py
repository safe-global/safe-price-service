from rest_framework import serializers

from .services.price_service import FiatPriceWithTimestamp


class TokenPriceResponseSerializer(serializers.Serializer):
    fiat_code = serializers.SerializerMethodField()
    fiat_price = serializers.CharField()
    timestamp = serializers.DateTimeField()

    def get_fiat_code(self, obj: FiatPriceWithTimestamp):
        return obj.fiat_code.name
