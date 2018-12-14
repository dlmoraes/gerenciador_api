# coding = utf-8

from rest_framework import serializers

from ..models import Ficha


class FichaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = (
        'nome','endereco', 'instalacao','status_inst', 'bairro', 'complemento','zona', 'classe', 'cc', 'email',
        'telefone', 'localidade','etapa', 'livro', 'sequencia','referencia', 'faturas','debito', 'cnr', 'total',
        'pddperdas', 'lf','medidor', 'bloq', 'e_baixarenda',
        #, , '',
        )
