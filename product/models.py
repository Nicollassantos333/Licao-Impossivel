from django.db import models
from django.contrib.auth.models import User

# Model para o Controle de Estoque
class Produto(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Produto")
    codigo_barras = models.CharField(max_length=50, unique=True, verbose_name="Código de Barras")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")
    preco = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, verbose_name="Preço Unitário")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    def __str__(self):
        return f"{self.nome} ({self.quantidade} un)"

# Model para o Histórico/Logs de Movimentação do Estoque por Usuário
class HistoricoEstoque(models.Model):
    METODOS = [
        ('ENTRADA', 'Entrada de Mercadoria'),
        ('SAIDA', 'Saída de Mercadoria'),
        ('AJUSTE', 'Ajuste de Inventário'),
    ]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="movimentacoes")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Operador")
    tipo_movimentacao = models.CharField(max_length=10, choices=METODOS)
    quantidade_alterada = models.IntegerField()
    motivo = models.TextField(blank=True, null=True)
    data_acao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.produto.nome}"
