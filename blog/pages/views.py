from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("INICIO")

def about(request):
    return HttpResponse("ABOUT")


def listar_pages(request):
    return HttpResponse("HOLA")
