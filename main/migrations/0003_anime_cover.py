# Generated by Django 5.0.2 on 2024-03-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_anime_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='cover',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]