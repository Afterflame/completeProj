# Generated by Django 3.1.6 on 2021-04-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feednotes', '0002_alter_note_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]