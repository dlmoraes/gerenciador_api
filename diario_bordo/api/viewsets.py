# coding = utf-8

from dateutil.parser import parse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from ..mixins import DiarioListCreateAPIMixin
from ..models import Diario
from .serializers import DiarioSerializers, DiariosSerializers, DiarioFormSerializers
from core.utils import formatoDeHoras

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DiarioViewSet(DiarioListCreateAPIMixin, ListCreateAPIView):
    queryset = Diario.objects.all()
    serializer_class = DiariosSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('dta_ocor', 'dta_concl', 'situacao', 'geracao_compl', 'motivo_causa', 'motivo_reducao',)
    ordering_fields = ('dta_ocor', 'dta_concl', 'situacao',)
    pagination_class = StandardResultsSetPagination

class DiarioRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiarioSerializers

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return DiarioFormSerializers
        return DiarioSerializers

    def get_object(self):
        pk = self.kwargs['id']
        return get_object_or_404(Diario, pk=pk)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        dados = request.data
        print(dados)
        conclusao = dados.get('dta_concl', None)
        if conclusao:
            dta_ocor = parse(dados['dta_ocor'])
            dados['situacao'] = 'CO'
            dta_concl = parse(dados['dta_concl'])
            dados['situacao'] = 'CO'
            diferenca = dta_concl - dta_ocor
            dados['hr_ocioso'] = formatoDeHoras(diferenca)
        else:
            dados['situacao'] = 'AT'
            dados['hr_ocioso'] = None

        dados['usu_mod'] = self.request.user.pk
        serializer = self.get_serializer(instance, data=dados, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
