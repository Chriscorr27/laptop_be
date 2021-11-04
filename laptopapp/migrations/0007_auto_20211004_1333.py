# Generated by Django 3.2.7 on 2021-10-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopapp', '0006_auto_20211004_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopmodel',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('IP', 'In Process'), ('OW', 'On the Way'), ('WC', 'With Customer'), ('C', 'Completed')], default='IP', max_length=2),
        ),
    ]
