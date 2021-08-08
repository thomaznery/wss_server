from django.shortcuts import render
from .tryd import context_init
import pickle
from rest_framework import status
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'marketdata/index.html', context_init())


@csrf_exempt
def state_att(request):
    if request.method == 'POST':
        data = request.POST["ativo"]
        print(data)
        return JsonResponse(None, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(None, status=status.HTTP_400_BAD_REQUEST)
