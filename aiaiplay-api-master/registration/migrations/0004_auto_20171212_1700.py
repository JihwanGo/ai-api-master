# Generated by Django 2.0 on 2017-12-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20171212_1700'),
        ('registration', '0003_auto_20171212_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='available_apps',
        ),
        migrations.RemoveField(
            model_name='license',
            name='available_contents',
        ),
        migrations.AddField(
            model_name='license',
            name='purchased_apps',
            field=models.ManyToManyField(blank=True, related_name='available_licenses', to='content.App', verbose_name='구매한 앱'),
        ),
        migrations.AddField(
            model_name='license',
            name='purchased_contents',
            field=models.ManyToManyField(blank=True, related_name='available_licenses', to='content.Content', verbose_name='구매한 콘텐츠'),
        ),
    ]
