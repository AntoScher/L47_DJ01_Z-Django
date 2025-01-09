# Generated by Django 5.1.4 on 2025-01-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'инсаданные', 'verbose_name_plural': 'Инсадерские данные'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='autor',
            field=models.CharField(default='default_author', max_length=200, verbose_name='Автор новости'),
            preserve_default=False,
        ),
    ]
