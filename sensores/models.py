from django.db import models

# Create your models here.
class RegistroSensorUmidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    valor = models.FloatField('Valor')
    class Meta:
        verbose_name = 'Registro de umidade'