# Generated by Django 4.0.6 on 2022-07-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]