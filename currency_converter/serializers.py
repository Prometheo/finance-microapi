from rest_framework import serializers
# from .models import Currency


class RequestConverterSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    amount = serializers.IntegerField()
    
# class CurrencyListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Currency
#         fields = '__all__'
