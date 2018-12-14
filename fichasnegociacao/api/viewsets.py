# coding = utf-8
from django_filters import rest_framework as filters, BaseInFilter, CharFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from ..models import Ficha
from .serializers import FichaSerializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_query_param = 'page_size'
    max_page_size = 1000


class CharInFilter(BaseInFilter, CharFilter):
    pass


class FichasFilter(filters.FilterSet):
    cc = CharInFilter(field_name='cc', lookup_expr='in')
    instalacao = CharInFilter(field_name='instalacao', lookup_expr='in')

    class Meta:
        model = Ficha
        fields = ['cc', 'instalacao']


class FichaListApiView(ListAPIView):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FichasFilter
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        resposta = Response(serializer.data)
        return resposta
