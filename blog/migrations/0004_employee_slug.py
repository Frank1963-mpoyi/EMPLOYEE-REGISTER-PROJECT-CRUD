# Generated by Django 3.0.8 on 2021-01-21 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210118_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
