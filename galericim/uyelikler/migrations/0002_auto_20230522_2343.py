# Generated by Django 3.1.2 on 2023-05-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uyelikler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='araba',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
