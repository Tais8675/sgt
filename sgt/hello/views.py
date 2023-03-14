from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, word!")
	
def greet(request,nome):
	return render(request, "tia_do_zap.html", {'name': nome, 'dia': datetime.time })

def ola(request):
    return render(request, "index.html")

#def tia_do_zap(request,nome):
	#return render(request, "tia_do_zap.html", {'name': nome, 'dia': datetime.time})

