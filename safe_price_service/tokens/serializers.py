from rest_framework import serializers


class TokenPriceResponseSerializer(serializers.Serializer):
    fiat_code = serializers.CharField()
    fiat_price = serializers.CharField()
    timestamp = serializers.DateTimeField()
