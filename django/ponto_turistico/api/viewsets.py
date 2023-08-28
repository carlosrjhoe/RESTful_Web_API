from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    