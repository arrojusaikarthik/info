# Generated by Django 3.2 on 2021-06-12 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0007_alter_allorderslist_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allorderslist',
            old_name='order_id',
            new_name='order_num',
        ),
    ]