# Generated by Django 3.1.2 on 2020-10-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]
