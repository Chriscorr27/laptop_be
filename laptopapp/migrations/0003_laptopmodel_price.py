# Generated by Django 3.2.7 on 2021-10-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopapp', '0002_auto_20211004_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]