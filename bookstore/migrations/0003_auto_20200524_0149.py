# Generated by Django 3.0 on 2020-05-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20200524_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(default='default.jpeg', upload_to='images'),
        ),
    ]
