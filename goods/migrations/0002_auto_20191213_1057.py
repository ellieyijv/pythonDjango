# Generated by Django 2.1.15 on 2019-12-13 10:57

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='content'),
        ),
    ]
