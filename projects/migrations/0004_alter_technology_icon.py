# Generated by Django 4.2 on 2024-11-16 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_technology_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.FileField(default='images/technologies/default.svg', upload_to='images/technologies/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpeg', 'jpg', 'webp', ''])], verbose_name='Technology Logo'),
        ),
    ]