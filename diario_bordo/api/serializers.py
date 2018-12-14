# coding = utf-8

from rest_framework import serializers

from ..models import Diario

class DiariosSerializers(serializers.ModelSerializer):
    usu_origem = serializers.StringRelatedField(many=False, read_only=True)
    usu_mod = serializers.StringRelatedField(many=False, read_only=True)
    situacao = serializers.SerializerMethodField()

    class Meta:
        model = Diario
        fields = ('id', 'usu_origem', 'usu_mod', 'dta_ocor',
                  'dta_concl', 'situacao', 'geracao_compl',
                  'hr_ocioso', 'motivo_causa', 'motivo_reducao',)

    def get_situacao(self, obj):
        return obj.get_situacao_display()

class DiarioSerializers(serializers.ModelSerializer):

    class Meta:
        model = Diario
        fields = ('id', 'usu_origem', 'usu_mod', 'dta_ocor',
                  'dta_concl', 'situacao', 'geracao_compl',
                  'hr_ocioso', 'motivo_causa', 'motivo_reducao',)

class DiarioFormSerializers(serializers.ModelSerializer):

    class Meta:
        model = Diario
        fields = '__all__'
