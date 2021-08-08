from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/state_att', views.state_att)
]
