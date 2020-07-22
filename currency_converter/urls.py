from django.urls import path
from . import views


urlpatterns = [
    path('convert_currency/', views.ConvertCurrency.as_view(), name='convert')
]