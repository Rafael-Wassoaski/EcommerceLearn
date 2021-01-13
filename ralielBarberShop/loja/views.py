from django.shortcuts import render
from .models import Produto, Categoria 

# Create your views here.



def index(req):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.filter(categoria = 'U')
    todasCategorias = Categoria.objects.all()
    categoriasHomems = Categoria.objects.filter(categoria = 'H')
    categoriasMulheres = Categoria.objects.filter(categoria = 'M')
    return render(req, '../templates/modules/home.html', {'todasCategorias': todasCategorias,'produtos': produtos,'categorias': categorias, 'categoriasHomems': categoriasHomems, 'categoriasMulheres': categoriasMulheres});
