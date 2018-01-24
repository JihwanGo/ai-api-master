from django.db import models

from content.models import Content, LauncherVersion, ContentVersion
from registration.models import License


class Log(models.Model):
    LOG_TYPES = [
        ('OL', 'Open Launcher'),
        ('CL', 'Close Launcher'),
        ('OC', 'Open Content'),
        ('CC', 'Close Content'),
        ('ER', 'Error'),
    ]

    type = models.CharField(
        verbose_name='타입',
        max_length=2,
        choices=LOG_TYPES,
    )
    timestamp = models.DateTimeField(
        verbose_name='시각',
        auto_now_add=True,
    )
    description = models.CharField(
        verbose_name='추가 설명',
        max_length=200,
        blank=True,
    )

    license = models.ForeignKey(
        verbose_name='라이센스',
        to=License,
        on_delete=models.DO_NOTHING,
        related_name='logs',
    )
    launcher_version = models.ForeignKey(
        verbose_name='런처 버전',
        to=LauncherVersion,
        on_delete=models.DO_NOTHING,
        related_name='logs',
    )
    content_version = models.ForeignKey(
        verbose_name='콘텐츠 버전',
        to=ContentVersion,
        on_delete=models.DO_NOTHING,
        related_name='logs',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = '로그'
        verbose_name_plural = '로그'

    def __str__(self):
        return '로그 #{}'.format(self.id)
