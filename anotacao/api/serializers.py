# coding = utf-8

from rest_framework import serializers

from ..models import Caderno, Etiqueta, Nota

class CadernoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Caderno
        fields = ('nome', 'usu_origem', 'favorito', 'dta_origem')

class EtiquetaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Etiqueta
        fields = ('nome', 'usu_origem', 'dta_origem',)

class NotaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = ('titulo', 'descricao', 'etiquetas', 'dta_origem',
                  'dta_mod', 'usu_mod')