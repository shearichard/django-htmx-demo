from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Todos Hello World")
    return render(request, "todospod/index.html",{})

