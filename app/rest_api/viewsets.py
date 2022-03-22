from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from app.rest_api.serialzers import StockSerializer
from app.models import Stock
from app.filters import StockFilter

# Create your views here.
class StockView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = StockFilter
    ordering_fields = ['name']