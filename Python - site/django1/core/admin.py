from django.contrib import admin
from .models import Produto
from .models import Cliente

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('Title','Price','Description','Inventory')

admin.site.register(Produto, ProdutoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Sobrenome', 'Idade', 'Email', 'Cpf', 'Identidade')
    

admin.site.register(Cliente, ClienteAdmin)