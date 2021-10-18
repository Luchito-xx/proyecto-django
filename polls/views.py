from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def index(request):
    doc_externo = get_template("index.html")
    documento = doc_externo.render()
    return HttpResponse(documento)

def home(request):
    return HttpResponse("que lo que")