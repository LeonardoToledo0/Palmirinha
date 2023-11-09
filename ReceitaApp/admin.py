from django.contrib import admin

from ReceitaApp.models import Receita,Categoria

# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['nome','grau_de_dificuldade', 'categoria']
    list_filter = ['nome', 'grau_de_dificuldade', 'categoria']
    list_display_links = ['nome','grau_de_dificuldade','categoria']






admin.site.register(Receita,ReceitaAdmin)
admin.site.register(Categoria)