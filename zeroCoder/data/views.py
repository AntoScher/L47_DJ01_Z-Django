from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data_view(request):
    return HttpResponse("This is the data page.")

def test_view(request):
    return HttpResponse("This is the test page.")
