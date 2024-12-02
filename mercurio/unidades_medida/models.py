from django.db import models
from mercurio.core.models import BaseModel


# Create your models here.
class UnidadeMedidaCategoria(BaseModel):
    nome = models.CharField(max_length=80)


class UnidadeMedida(BaseModel):
    nome = models.CharField(max_length=80)
    sigla = models.CharField(max_length=5)
    categoria = models.ForeignKey(UnidadeMedidaCategoria, on_delete=models.CASCADE)
    multiplicador = models.FloatField()
    divisor = models.FloatField()
    unidade_base = models.BooleanField(default=False)
    multiplo = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='aumenta_base')
    submultiplo = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='diminui_base')