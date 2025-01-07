from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def data_view(request):
    return render(request, 'data/data.html', {'caption1':"Белый орел"})
def test_view(request):
    return render(request, 'data/test.html', {'caption1':"Белый орел",'caption2':"птенцов орла"})