# Generated by Django 4.1 on 2023-07-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d', verbose_name='Image'),
        ),
    ]
