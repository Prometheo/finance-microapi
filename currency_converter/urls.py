from django.urls import path
from . import views


urlpatterns = [
    path('convert_currency/', views.ConvertCurrency.as_view(), name='convert'),
    path('list_currencies/', views.ListCurrencies.as_view())
]