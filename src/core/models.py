from django.db import models

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=200)
    email = models.EmailField("E-mail", unique=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado_em", auto_now=True)

    def __str__(self):
        return self.nome
