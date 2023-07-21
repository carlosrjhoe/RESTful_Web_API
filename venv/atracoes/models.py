from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150, blank=True)
    descricao = models.TextField(blank=True)
    horario_func = models.TextField(blank=True)
    idade_minima = models.IntegerField(blank=True)

    def __str__(self):
        return self.nome