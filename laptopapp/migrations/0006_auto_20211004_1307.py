# Generated by Django 3.2.7 on 2021-10-04 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptopapp', '0005_auto_20211004_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='start_data',
            new_name='start_date',
        ),
    ]
