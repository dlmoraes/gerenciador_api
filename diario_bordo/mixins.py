# coding = utf-8

from dateutil.parser import parse
from rest_framework import status
from rest_framework.response import Response

from .models import Diario
from .api.serializers import DiariosSerializers, DiarioFormSerializers
from core.utils import formatoDeHoras

class DiarioListCreateAPIMixin(object):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DiarioFormSerializers
        return DiariosSerializers


    def create(self, request, *args, **kwargs):
        dados = request.data

        if dados.get('dta_concl', None):
            dta_ocor = parse(dados['dta_ocor'])
            dta_concl = parse(dados['dta_concl'])
            dados['situacao'] = 'CO'
            diferenca = dta_concl - dta_ocor
            dados['hr_ocioso'] = formatoDeHoras(diferenca)

        usuario = self.request.user

        dados['usu_origem'] = usuario.pk
        dados['usu_mod'] = usuario.pk

        serializer = self.get_serializer(data=dados)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)