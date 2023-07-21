from django.db import models

# Create your models here.
class Endereco(models.Model):
    linha_1 = models.CharField(max_length=150)
    linha_2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    latidude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.linha_1