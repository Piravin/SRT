# Generated by Django 3.0.7 on 2020-06-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='year',
            field=models.CharField(max_length=20),
        ),
    ]