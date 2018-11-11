from rest_framework.viewsets import ModelViewSet
from sensores.models import RegistroSensorUmidade
from .serializers import RegistroSensorUmidadeSerializer 

class RegistroSensorUmidadeViewSet(ModelViewSet):
    queryset = RegistroSensorUmidade.objects.all()
    serializer_class = RegistroSensorUmidadeSerializer

