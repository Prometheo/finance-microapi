from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views, generics
from rest_framework.views import APIView
from .serializers import RequestConverterSerializer
from drf_yasg.utils import swagger_auto_schema
from finance_microapi.settings import CURR_API
# from .models import Currency
# from .serializers import CurrencyListSerializer
from datetime import date

RESPONSES = {
    '200': 'currency converted successfully.',
    '400': 'Incorrect request format.',
    '500': 'An error occurred, could convert.' 
}

# Create your views here.
def Converter_func(from_currency, to_currency, amount):
    cur_param = from_currency + '_' + to_currency
    query_param = {'q':cur_param, 'compact':'ultra', 'apiKey':CURR_API} 
    _url = 'https://free.currconv.com/api/v7/convert'
    try:
        api_call = requests.request('get', _url, params=query_param)
        result = api_call.json()
        base_conversion = result.get(cur_param)
        final_conversion = base_conversion * amount
        data = {
            'status':'Success',
            'info':{
                'rate':base_conversion,
                'date':date.today()
            },
            'result':final_conversion
        }
        return data
    except:
        error_data = {
            'ERROR': 'process was interrupted, please re-submit'
        }
        return error_data


class ConvertCurrency(views.APIView):

    @swagger_auto_schema(
        request_body=RequestConverterSerializer,
        operation_summary="Convert currency",
        operation_description="",
        responses=RESPONSES,
        tags=['Convert']
    )

    def post(self, request):
        serializer = RequestConverterSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            from_currency = validated_data.get('from_currency')
            to_currency = validated_data.get('to_currency')
            amount = validated_data.get('amount')
            data = Converter_func(from_currency, to_currency, amount)
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'failed',
                'data': { 'message': 'Incorrect request format.', 'errors': serializer.errors}
            }, status=status.HTTP_400_BAD_REQUEST)


class ListCurrencies(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a list of all currencies",
        operation_description="",
        responses=RESPONSES,
        tags=['List Currencies']
    )

    # def get(self, request, format=None):
    #     queryset = Currency.objects.all()
    #     serializer = CurrencyListSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        url = 'https://free.currconv.com/api/v7/currencies'
        query_params = {'apiKey':CURR_API} 
        response =  requests.request('get', url, params=query_params)
        currencies = response.json()

        return Response({
            'status': 'Success',
            'data': currencies
        })
