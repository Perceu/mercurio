from django.db import models
from mercurio.core.models import BaseModel


# Create your models here.

class UnidadeMedida(BaseModel):
    nome = models.CharField(max_length=80)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nome}"
    
class UnidadeMedidaConversoes(BaseModel):
    unidade_origem = models.ForeignKey(UnidadeMedida, related_name='origem', on_delete=models.CASCADE)
    unidade_destino = models.ForeignKey(UnidadeMedida, related_name='destino', on_delete=models.CASCADE)
    multiplicador = models.FloatField()

    def __str__(self):
        return f"{self.unidade_origem} -> {self.unidade_destino}"