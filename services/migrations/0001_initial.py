# Generated by Django 5.0.1 on 2024-01-28 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Service Name')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='Service Safe URL')),
                ('desc', models.TextField(verbose_name='Service Description')),
                ('icon', models.ImageField(default='images/services/default.png', upload_to='images/services/', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='Service Image')),
                ('icon_alt', models.CharField(max_length=255, verbose_name='Service Icon Alternative Text')),
                ('priority', models.PositiveSmallIntegerField(unique=True, verbose_name='Service Display Order/Priority')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
