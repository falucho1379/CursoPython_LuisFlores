# Generated by Django 4.1.3 on 2022-11-22 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_birth',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='expire_date',
        ),
    ]
