from django.db import models


class Corretora(models.Model):
    id = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=255)
    color = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.id}-{self.nome}'


class Agressor(models.TextChoices):
    COMPRADOR = 'C'
    VENDEDOR = 'V'
    LEILAO = 'L'


class Status_estrategia(models.TextChoices):
    ON = 'ON'
    OFF = 'OFF'


class Estrategia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=155)
    status = models.CharField(max_length=3, choices=Status_estrategia.choices)
    created = models.DateTimeField(auto_now_add=True)


class wss_signal(models.Model):
    created = models.DateTimeField(primary_key=True, auto_now_add=True)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    ativo = models.CharField(max_length=15)
    preco = models.DecimalField(max_digits=11, decimal_places=2)


class wdo_book(models.Model):
    numero = models.BigIntegerField()
    ativo = models.CharField(max_length=6, default='null')
    hora = models.DateTimeField()
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    comprador = models.PositiveIntegerField()
    vendedor = models.PositiveIntegerField()
    agressor = models.CharField(max_length=1, choices=Agressor.choices, default=Agressor.LEILAO)

    def __str__(self):
        return f'{self.agressor}: {self.ativo}: {self.preco}'


class win_book(models.Model):
    numero = models.BigIntegerField()
    ativo = models.CharField(max_length=6)
    hora = models.DateTimeField()
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    comprador = models.PositiveIntegerField()
    vendedor = models.PositiveIntegerField()
    agressor = models.CharField(max_length=1, choices=Agressor.choices, default=Agressor.LEILAO)

    def __str__(self):
        return f'{self.agressor}: {self.ativo}: {self.preco}'
