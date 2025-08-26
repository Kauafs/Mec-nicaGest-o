from django.db import models
from django.contrib.auth.models import User
from loja.models import Peca

class BuyPecas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto} - {self.preco} cada"
