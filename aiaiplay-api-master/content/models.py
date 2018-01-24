from string import digits

from django.core.exceptions import ValidationError
from django.db import models


# TODO: Create VersionNumber custom field


def version_number_validator(value):
    allowed_chars = digits + '.'
    for char in value:
        if char not in allowed_chars:
            raise ValidationError('버전명은 숫자 혹은 "."만 포함할 수 있습니다.')


class App(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='ID',
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=30,
    )

    class Meta:
        verbose_name = '앱'
        verbose_name_plural = '앱'

    def __str__(self):
        return self.name

    def num_distributions(self):
        return self.available_licenses.count()

    num_distributions.short_description = '사용 중인 라이센스의 수'


class Content(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='ID',
        primary_key=True,
    )
    app = models.ForeignKey(
        verbose_name='앱',
        to=App,
        on_delete=models.DO_NOTHING,
        related_name='contents',
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )
    scene_name = models.CharField(
        verbose_name='Unity Scene 이름',
        max_length=50,  # TODO: To be updated
    )
    asset_bundle_name = models.CharField(
        verbose_name='Asset Bundle 이름',
        max_length=50,
    )

    class Meta:
        verbose_name = '콘텐츠'
        verbose_name_plural = '콘텐츠'

    def __str__(self):
        return '{} ({})'.format(self.name, self.app)

    def latest_version(self):
        return self.versions.latest('update_time')

    latest_version.short_description = '최신 버전'

    def num_distributions(self):
        return self.available_licenses.count()

    num_distributions.short_description = '사용 중인 라이센스의 수'


class AbstractVersion(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='ID',
        primary_key=True,
    )
    version_number = models.CharField(
        verbose_name='버전명',
        max_length=8,
        validators=[version_number_validator],
    )
    download_url = models.URLField(
        verbose_name='다운로드 URL',
    )
    update_time = models.DateTimeField(
        verbose_name='업데이트 시간',
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class LauncherVersion(AbstractVersion):
    class Meta:
        verbose_name = '런처 버전'
        verbose_name_plural = '런처 버전'

    def __str__(self):
        return 'Launcher v{}'.format(self.version_number)


class ContentVersion(AbstractVersion):
    content = models.ForeignKey(
        verbose_name='콘텐츠',
        to=Content,
        on_delete=models.SET_NULL,
        related_name='versions',
        null=True,
    )
    minimum_launcher_version = models.ForeignKey(
        verbose_name='최소 런처 버전',
        to=LauncherVersion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    asset_bundle_number = models.PositiveIntegerField(
        verbose_name='Asset Bundle 번호',
    )

    class Meta:
        unique_together = ('content', 'asset_bundle_number')
        verbose_name = '콘텐츠 버전'
        verbose_name_plural = '콘텐츠 버전'

    def __str__(self):
        return '{} v{}'.format(self.content.name, self.version_number)
