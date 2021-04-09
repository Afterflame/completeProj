# Generated by Django 3.2 on 2021-04-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=32)),
                ('body', models.TextField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
