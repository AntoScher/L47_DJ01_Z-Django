from django.shortcuts import render
from .models import News_post


def data_view(request):
    news = News_post.objects.all()  # получить все новости из базы данных
    return render(request, 'data/data.html', {'caption1':"Белый орел",'news': news})
def ad_data(request):
    return render(request, 'data/addata.html', {'caption1':"Белый орел",'caption2':"птенцов орла"})

