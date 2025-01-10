from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'autor', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости', 'style': 'color: white;'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости', 'style': 'color: white;'}),
            'autor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор новости', 'style': 'color: white;'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости', 'style': 'color: white;'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации', 'style': 'color: white;'})
        }

"""class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'short_description','autor', 'text', 'pub_date']



widgets = {
        'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости', 'style': 'color: white !important;'}),
        'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости', 'style': 'color: white;'}),
        'autor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор новости', 'style': 'color: white;'}),
        'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание новости', 'style': 'color: white;'}),
        'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации', 'style': 'color: white;'})
    }"""
