# Generated by Django 4.0.6 on 2022-07-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_award'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
