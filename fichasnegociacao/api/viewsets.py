# coding = utf-8

from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from ..models import Ficha
from .serializers import FichaSerializers

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 1000

class FichaListApiView(ListAPIView):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('instalacao', 'cc',)
    pagination_class = StandardResultsSetPagination