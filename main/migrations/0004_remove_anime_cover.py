# Generated by Django 5.0.2 on 2024-03-04 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_anime_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='cover',
        ),
    ]
