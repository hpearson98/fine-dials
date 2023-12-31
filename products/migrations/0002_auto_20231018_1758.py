# Generated by Django 3.2.21 on 2023-10-18 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='crystal',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='watch',
            name='gender',
            field=models.CharField(choices=[('MENS', "Men's"), ('WOMENS', "Woman's")], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='watch',
            name='style',
            field=models.CharField(choices=[('DIVER', 'Diver'), ('DRESS', 'Dress'), ('CHRONOGRAPH', 'Chronograph'), ('PILOT/FIELD', 'Pilot/Field'), ('GMT', 'GMT'), ('CASUAL', 'Casual'), ('DIGITAL', 'Digital')], default='', max_length=30),
        ),
    ]
