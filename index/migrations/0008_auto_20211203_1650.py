# Generated by Django 3.2.9 on 2021-12-03 15:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20211203_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='text_ca',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='text_es',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
