from django.contrib import admin
from mercurio.unidades_medida.models import UnidadeMedida, UnidadeMedidaConversoes
# Register your models here.

admin.site.register(UnidadeMedida)
admin.site.register(UnidadeMedidaConversoes)