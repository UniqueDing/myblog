# Generated by Django 3.0.3 on 2020-02-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200216_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
