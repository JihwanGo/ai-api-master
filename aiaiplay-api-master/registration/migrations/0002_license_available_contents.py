# Generated by Django 2.0 on 2017-12-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='available_contents',
            field=models.ManyToManyField(blank=True, related_name='available_licenses', to='content.Content'),
        ),
    ]
