from django.shortcuts import render
from .models import Produto, Categoria 

# Create your views here.



def index(req):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    categoriasHomems = Categoria.objects.filter(categoria = 'H')
    print(categoriasHomems)
    return render(req, '../templates/modules/home.html', {'produtos': produtos,'categorias': categorias, 'categoriasHomems': categoriasHomems});
