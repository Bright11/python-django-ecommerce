# Generated by Django 4.0.3 on 2022-05-08 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sekking_price',
            new_name='striping_price',
        ),
    ]
