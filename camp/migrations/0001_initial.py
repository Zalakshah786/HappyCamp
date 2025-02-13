# Generated by Django 4.2.19 on 2025-02-13 17:42

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('age_group_min', models.IntegerField()),
                ('age_group_max', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('daily_schedule', models.TextField(blank=True, null=True)),
                ('capacity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(default=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('available_spots', models.PositiveIntegerField(default=0)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
        ),
    ]
