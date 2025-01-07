from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html') # HttpResponse("<h1>Это мой первый проект на Django</h1>")
def contact(request):
    return render(request, 'core/contact.html') # HttpResponse("<h1>Это контакты моего проекта на Django</h1>")