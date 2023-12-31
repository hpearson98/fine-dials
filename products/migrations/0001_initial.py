# Generated by Django 3.2.21 on 2023-10-16 18:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('country_of_origin', models.CharField(max_length=30)),
                ('year_established', models.IntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2023)])),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('movement', models.CharField(choices=[('AUTO', 'Automatic'), ('QUARTZ', 'Quartz')], max_length=30)),
                ('calibre', models.CharField(blank=True, max_length=30)),
                ('water_resistance', models.CharField(max_length=5)),
                ('other_features', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]
