from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField("Estoque", default=0)
    criado_em = models.DateField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Produtos"
        verbose_name_plural = "Produtos"
        ordering = ["-criado_em"]

    def _str_(self):
        return self.nome
