from django.contrib import admin
from .models import Produto, HistoricoEstoque

# Exibe a tabela de Produtos no painel administrativo
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_barras', 'quantidade', 'preco', 'data_atualizacao')
    search_fields = ('nome', 'codigo_barras')
    list_filter = ('data_atualizacao',)

# Exibe a tabela de Histórico de Estoque
@admin.register(HistoricoEstoque)
class HistoricoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'tipo_movimentacao', 'quantidade_alterada', 'data_acao')
    list_filter = ('tipo_movimentacao', 'data_acao')
    search_fields = ('produto__nome', 'usuario__username')
