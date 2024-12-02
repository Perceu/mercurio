from django.db import models
from mercurio.core.models import BaseModel
from mercurio.produtos.models import Produto
from mercurio.unidades_medida.models import UnidadeMedida

# Create your models here.
class Estoque(BaseModel):
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade_calculada = models.FloatField()

    def __str__(self):
        return f"{self.produto}"

class EstoqueMovimentos(BaseModel):
    estoque = models.ForeignKey(Estoque, related_name='movimentos', on_delete=models.CASCADE)
    data_movimento = models.DateTimeField()
    entrada = models.BooleanField(default=False)
    saida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.estoque.produto} mov {self.pk}"


class EstoqueMovimentosLotes(BaseModel):
    movimento = models.ForeignKey(EstoqueMovimentos, related_name='lotes', on_delete=models.CASCADE)
    quantidade = models.FloatField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.RESTRICT)
    vencimento = models.DateField()

    def __str__(self):
        return f"{self.movimento.estoque.produto} lote {self.pk}"