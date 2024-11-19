from django.urls import path

from . import views

app_name = 'countpod'

urlpatterns = [
    path('', views.index, name='index'),
    path('countup', views.countup, name='countup'),
    path('countdown', views.countdown, name='countdown'),
    path('count', views.count, name='count'),
]


