from django.contrib import admin
from mercurio.estoques.models import Estoque, EstoqueMovimentos, EstoqueMovimentosLotes
# Register your models here.

admin.site.register(Estoque)
admin.site.register(EstoqueMovimentos)
admin.site.register(EstoqueMovimentosLotes)
