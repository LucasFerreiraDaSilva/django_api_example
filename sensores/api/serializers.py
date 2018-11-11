from rest_framework.serializers import ModelSerializer
from sensores.models import RegistroSensorUmidade


class RegistroSensorUmidadeSerializer(ModelSerializer):
    class Meta:
        model = RegistroSensorUmidade
        fields = ('id', 'timestamp', 'valor')