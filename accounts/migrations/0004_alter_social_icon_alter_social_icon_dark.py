# Generated by Django 4.2 on 2024-11-16 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user_alter_social_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='icon',
            field=models.FileField(default='images/icons/default.svg', upload_to='images/icons/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', ''])], verbose_name='Social Media Icon'),
        ),
        migrations.AlterField(
            model_name='social',
            name='icon_dark',
            field=models.FileField(blank=True, null=True, upload_to='images/icons/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', ''])], verbose_name='Social Media Dark Icon'),
        ),
    ]
