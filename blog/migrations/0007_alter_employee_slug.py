# Generated by Django 3.2 on 2021-05-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(),
        ),
    ]