# Generated by Django 4.1.1 on 2022-09-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='uid',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]