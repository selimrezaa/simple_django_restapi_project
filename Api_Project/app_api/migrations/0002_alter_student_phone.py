# Generated by Django 3.2.8 on 2021-10-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
