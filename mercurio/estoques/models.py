from django.db import models
from mercurio.core.models import BaseModel
from mercurio.produtos.models import Produto
from mercurio.unidades_medida.models import UnidadeMedida

# Create your models here.
class Estoque(BaseModel):
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade_calculada = models.FloatField()

class EstoqueMovimentos(BaseModel):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    data_movimento = models.DateTimeField()
    entrada = models.BooleanField(default=False)
    saida = models.BooleanField(default=False)


class EstoqueMovimentosLotes(BaseModel):
    movimento = models.ForeignKey(EstoqueMovimentos, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.RESTRICT)
    vencimento = models.DateField()