from rest_framework.serializers import ModelSerializer
from ponto_turistico.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer 

class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True, read_only=True)
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'atracoes']
        