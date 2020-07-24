import requests
from django.core.management.base import BaseCommand
from currency_converter.models import Currency
from finance_microapi.settings import CURR_API

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        _url = 'https://free.currconv.com/api/v7/countries'
        query_params = {'apiKey':CURR_API}
        data = requests.request('get', _url, params=query_params)
        data = data.json()
        data = data['results']
        for entry in data:
                Currency.objects.create(country_name=data[entry]['name'], 
                                        currency_symbol=data[entry]['currencySymbol'], 
                                        currency_name=data[entry]['currencyName'], 
                                        currency_id=data[entry]['currencyId'])