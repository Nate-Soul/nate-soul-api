# Generated by Django 5.0.1 on 2024-01-28 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('incomplete', 'Incomplete')], max_length=100, verbose_name='Project Completion Status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('client', 'Client'), ('hubby', 'Hubby'), ('side', 'Side')], max_length=100, verbose_name='Project Type'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.FileField(default='images/technologies.default.png', upload_to='images/technologies/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpeg', 'jpg', 'webp'])], verbose_name='Technology Logo'),
        ),
    ]
