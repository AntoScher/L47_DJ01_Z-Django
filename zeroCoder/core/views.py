from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html') # HttpResponse("<h1>Это мой первый проект на Django</h1>")
def contact(request):
    return HttpResponse("<h1>Это контакты моего проекта на Django</h1>")