# Generated by Django 4.0.5 on 2022-06-05 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='message_id',
        ),
    ]