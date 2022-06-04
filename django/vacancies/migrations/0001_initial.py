# Generated by Django 4.0.5 on 2022-06-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название вакансии')),
                ('desc', models.TextField(verbose_name='Описание вакансии')),
                ('add_date', models.DateTimeField(auto_now=True, verbose_name='Дата добавления вакансии')),
                ('salary', models.PositiveIntegerField(verbose_name='Заработная плата')),
                ('remote', models.BooleanField(default=True, verbose_name='Удаленная работа')),
                ('relocation', models.BooleanField(default=True, verbose_name='Рабочая релокация')),
                ('employment', models.CharField(choices=[('FULLDAY', 'Полный день'), ('NOTFULL', 'Неполный день'), ('PRJ', 'Проектная занятость'), ('OFFULL', 'Частичная занятость')], max_length=7, verbose_name='Занятость')),
                ('skill', models.CharField(choices=[('JR', 'Junior'), ('MD', 'Middle'), ('SR', 'Senior'), ('TL', 'TeamLead')], max_length=2, verbose_name='Уровень девелопмента')),
                ('tasks', models.TextField(verbose_name='Задачи')),
                ('requirements', models.TextField(verbose_name='Требования')),
                ('contact', models.URLField(verbose_name='Ссылка на работодателя')),
                ('url', models.SlugField(verbose_name='Адрес вакансии')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-add_date'],
            },
        ),
    ]
