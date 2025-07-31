from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display  = ("nome", "preco", "quantidade_estoque", "criado_em")
    search_fields = ("nome",)
    list_filter   = ("criado_em",)
