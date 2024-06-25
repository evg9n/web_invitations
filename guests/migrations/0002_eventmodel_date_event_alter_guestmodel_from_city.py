# Generated by Django 5.0.1 on 2024-06-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='date_event',
            field=models.TimeField(blank=True, null=True, unique=True, verbose_name='Время начала события'),
        ),
        migrations.AlterField(
            model_name='guestmodel',
            name='from_city',
            field=models.ManyToManyField(blank=True, to='guests.citymodel', verbose_name='С какого города забрать на мероприятие?'),
        ),
    ]