from django.urls import path

from . import views

app_name = 'todospod'

urlpatterns = [
    path('', views.index, name='index'),
]


