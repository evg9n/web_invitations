# Generated by Django 5.0.1 on 2024-06-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_eventmodel_date_event_alter_guestmodel_from_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='date_event',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='date',
            field=models.DateField(blank=True, null=True, unique=True, verbose_name='Дата начала события'),
        ),
    ]
