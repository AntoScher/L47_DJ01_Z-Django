from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html', {'caption1':"Белый орел"})
def contact(request):
    return render(request, 'core/contact.html', {'caption1':"Белый орел",'caption2':"птенцов орла"})