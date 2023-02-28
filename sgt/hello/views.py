from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, word!")
	
def greet(request,nome):
	return HttpResponse("Ola " + nome)
