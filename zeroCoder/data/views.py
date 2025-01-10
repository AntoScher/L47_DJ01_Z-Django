from django.shortcuts import render
from .models import News_post
from .forms import News_postForm
from django.shortcuts import redirect


def data_view(request):
    news = News_post.objects.all()  # получить все новости из базы данных
    return render(request, 'data/data.html', {'caption1':"Белый орел",'news': news})
def ad_data(request):
	error=""
	if request.method == 'POST':
		form = News_postForm(request.POST) # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('data')
		else:
			error = "Данные были заполнены некорректно"
	form = News_postForm()
	return render(request, 'data/addata.html', {'form': form, 'error': error})


"""def ad_data(request):
    form=News_postForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('data')
    return render(request, 'data/addata.html', {'caption1':"Белый орел",'caption2':"птенцов орла",'form': form})"""

