from django.shortcuts import render
from ReceitaApp.models import Receita, Categoria

# Create your views here.



def index(request):
    # Açoes da minha view
    return render(request,'index.html')
   
     





def receitas(request):
# Dicionario contendo as informações que iremos usar no template
# Buscar as receitas no banco 
    lista_receitas = Receita.objects.all()
    context = {
        'receitas': lista_receitas,
       }
    return render(request, 'receitas.html', context)

def detalhes_receita(request,id):
    # buscar a receita pelo id informando
    receita = Receita.objects.get(id = id)
    context = {
        'receita': receita
    }
    return render(request, 'receita.html', context)

