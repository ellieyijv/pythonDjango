# Generated by Django 2.1.15 on 2020-02-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20200131_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Add Time'),
        ),
    ]
