from django.shortcuts import render
from mercurio.produtos.models import Produto
from mercurio.estoques.models import Estoque


# Create your views here.
def home_teste(request):

    produto = Produto.objects.first()

    estoque = Estoque.objects.filter(produto = produto).get()
    total_saidas = 0
    total_entradas = 0
    for movimento in estoque.movimentos.all():
        if movimento.entrada:
            for lote in movimento.lotes.all():
                total_entradas += lote.quantidade
        else:
            for lote in movimento.lotes.all():
                total_saidas += lote.quantidade


    return render(request,  'teste.html', {
        'produto': produto.nome,
        'calculo_resultado': total_entradas - total_saidas
    })