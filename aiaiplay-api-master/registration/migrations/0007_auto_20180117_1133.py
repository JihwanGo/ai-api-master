# Generated by Django 2.0 on 2018-01-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20180117_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=100, verbose_name='기관명'),
        ),
        migrations.AlterField(
            model_name='license',
            name='description',
            field=models.CharField(max_length=100, verbose_name='설명'),
        ),
    ]
