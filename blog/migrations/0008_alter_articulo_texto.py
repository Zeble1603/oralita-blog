# Generated by Django 3.2.9 on 2021-11-24 18:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211124_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]