# Generated by Django 3.2.9 on 2021-11-28 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20211128_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidad',
            name='alt_img_ca',
        ),
        migrations.RemoveField(
            model_name='especialidad',
            name='alt_img_es',
        ),
    ]
