# Generated by Django 3.2 on 2021-06-06 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_logos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logos',
            name='dateandthetime',
        ),
        migrations.RemoveField(
            model_name='logos',
            name='details',
        ),
        migrations.RemoveField(
            model_name='logos',
            name='logodetails',
        ),
    ]
