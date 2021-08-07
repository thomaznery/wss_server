from queue import Queue
from helper.AcumuladorHelper import *
from threading import Thread
from .socket import *
from helper.ClockHelper import CHelper
from .models import Corretora, Negocio


# lista de corretoras monitoras pelo sistema, apenas corretas grandes que movimentam o mercado
# nao olhamos para corretoras, pequenas, como Clear, Modal
corretoras = {
    0: 'Agente nao monitorado',
    122: 'BGC Liquidez',
    85: 'BTG',
    72: 'Bradesco',
    6003: 'C6',
    88: 'Capital',
    45: 'Credit',
    120: 'Genial',
    238: 'Goldman',
    1130: 'Intl',
    114: 'Itau',
    16: 'JpMorgan',
    13: 'Merril',
    40: 'Morgan',
    23: 'Necton',
    92: 'Renascenca',
    27: 'Santander',
    127: 'Tullet',
    8: 'UBS',
    3: 'XP'
}

PONTO_MINI_DOLAR = 10
PONTO_MINI_INDICE = 0.20
TEMPO_GRAFICO = 5
""""
    Classe com funcao de ler e acumular todos os negocios dos dias, separados por corretora
"""
# quando o resto da divisao dos minutos por 5 foir igual a zero, executar

ch = CHelper()
_NOME = 'Times and Trader WSS'


class acumula(Thread):
    def __init__(self, ativo) -> None:
        Thread.__init__(self)
        self.agentes = Corretora.objects.order_by('id')
        self.ativo = ativo.upper()
        self.qtd_agressao_compra_dia = 0
        self.qtd_agressao_venda_dia = 0
        self.volume_total = 0

    # receber o negocio e enviar ao coletor

    def run(self):
        cont = 0
        # while ch.is_pregao_aberto():
        cont += 1
        negocio = ultimo_negocio(self.ativo)
        self.colector(negocio)

    # fazer a analise do negocio e direcionado ao agente agressor
    def colector(self, negocio):
        agressor = negocio['agressor']
        preco = negocio['preco']
        comprador = negocio['comprador']
        vendedor = negocio['vendedor']
        quantidade = int(negocio['qntd'])
        negocio_model = Negocio(
            preco, negocio['hora'], quantidade, comprador, vendedor, agressor)

        negocio_model.save()
