import re
from .models import Corretora


def context_init():

    corretoras = Corretora.objects.order_by('id')

    context = {
        'corretoras': corretoras
    }
    return context
