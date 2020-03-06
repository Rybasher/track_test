# Generated by Django 3.0.4 on 2020-03-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Новость')),
                ('content', models.TextField(help_text='Заполните описание', verbose_name='Текст поста')),
                ('published_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published_date'],
                'unique_together': {('published_date',)},
            },
        ),
    ]
