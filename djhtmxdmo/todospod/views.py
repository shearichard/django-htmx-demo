from random import randrange

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Todos Hello World")
    rnd_int = randrange(10000000)
    return render(request, f"todospod/index.html",{})

