# Generated by Django 3.2.7 on 2021-10-04 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptopapp', '0003_laptopmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('IP', 'In Process'), ('OW', 'On the Way'), ('WC', 'With Customer'), ('C', 'Completed')], max_length=2)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptopapp.laptopmodel')),
            ],
        ),
    ]