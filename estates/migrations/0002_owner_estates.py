# Generated by Django 3.2.7 on 2021-09-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='estates',
            field=models.ManyToManyField(to='estates.Estate'),
        ),
    ]
