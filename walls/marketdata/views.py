
from django.shortcuts import render
from .models import Corretora
from .tryd import context_init
# Create your views here.


def index(request):
    corretoras = Corretora.objects.order_by('id')
    context = context_init()
    return render(request, 'marketdata/index.html', context)
