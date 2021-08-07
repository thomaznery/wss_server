from django.db import models


class VencimentosDolar(models.TextChoices):
    JANEIRO = 'F'
    FEVEREIRO = 'G'
    MARCO = 'H'
    ABRIL = 'J'
    MAIO = 'K'
    JUNHO = 'M'
    JULHO = 'N'
    AGOSTO = 'Q'
    SETEMBRO = 'U'
    OUTUBRO = 'V'
    NOVEMBRO = 'X'
    DEZEMBRO = 'Z'


class VencimentosIndice(models.TextChoices):
    FEVEREIRO = 'G'
    ABRIL = 'J'
    JUNHO = 'M'
    AGOSTO = 'Q'
    OUTUBRO = 'V'
    DEZEMBRO = 'Z'


class Agressor(models.TextChoices):
    COMPRADOR = 'C'
    VENDEDOR = 'V'
    LEILAO = 'L'


class StatusIndice(models.TextChoices):
    VENCIDO = 1
    ATUAL = 2


class WDO(models.Model):
    ticket = models.CharField(primary_key=True, max_length=7)
    vencimento_dt = models.DateField(auto_now=False)
    vencimento = models.CharField(max_length=1, choices=VencimentosDolar.choices)
    status = models.CharField(max_length=100, choices=StatusIndice.choices)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket


class WIN(models.Model):
    ticket = models.CharField(primary_key=True, max_length=7)
    vencimento_dt = models.DateField(auto_now=False)
    vencimento = models.CharField(max_length=1, choices=VencimentosIndice.choices)
    status = models.CharField(max_length=100, choices=StatusIndice.choices)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket


class Corretora(models.Model):
    id = models.SlugField(primary_key=True)
    nome = models.CharField(max_length=255)
    color = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.id}-{self.nome}'


class Negocio(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hora = models.DateField(auto_now=False)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    comprador = models.PositiveIntegerField()
    vendedor = models.PositiveIntegerField()
    agressor = models.CharField(max_length=1, choices=Agressor.choices)
