from .socket import ultimo_negocio
from .models import WDO, WIN, Corretora


def context_init():
    dolar = WDO.objects.get(status='1')
    last_dolar = ultimo_negocio(ativo=dolar.ticket)

    indice = WIN.objects.get(status='1')
    last_ind = ultimo_negocio(ativo=indice.ticket)

    corretoras = Corretora.objects.order_by('id')

    context = {
        'corretoras': corretoras
    }
    return context
