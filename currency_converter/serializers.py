from rest_framework import serializers


class RequestConverterSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    amount = serializers.IntegerField()
    