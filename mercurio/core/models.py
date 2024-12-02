from django.db import models
from django.conf import settings

# Create your models here.
class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_criado_por', on_delete=models.RESTRICT)
    alterado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modificado_por', null=True, blank=True, on_delete=models.RESTRICT)

    class Meta:
        abstract= True