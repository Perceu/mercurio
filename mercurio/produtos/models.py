from django.db import models
from mercurio.core.models import BaseModel
from mercurio.unidades_medida.models import UnidadeMedida

# Create your models here.
class Produto(BaseModel):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(default='', blank=True)
    armazenamento_base = models.ForeignKey(UnidadeMedida, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.nome}, armazenada em ({self.armazenamento_base.sigla})"