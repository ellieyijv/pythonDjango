# Generated by Django 2.1.15 on 2019-12-13 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191213_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='Category'),
        ),
    ]
