from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

from content.models import App, Content


class User(AbstractUser):
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'


class Institution(models.Model):
    id = models.PositiveIntegerField(
        verbose_name='ID',
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='기관명',
        max_length=100,
    )

    class Meta:
        verbose_name = '기관'
        verbose_name_plural = '기관'

    def __str__(self):
        return self.name

    def num_licenses(self):
        return self.licenses.count()

    num_licenses.short_description = '라이센스 개수'


class License(models.Model):
    key = models.CharField(
        verbose_name='라이센스 키',
        max_length=30,
        primary_key=True,
    )
    description = models.CharField(
        verbose_name='설명',
        max_length=100,
    )
    unity_key = models.CharField(
        verbose_name='기기별 Unity 키',
        max_length=100,  # TODO: To be updated
        null=True,
        blank=True,
    )

    register_time = models.DateTimeField(
        verbose_name='최초 등록 시각',
        null=True,
        blank=True,
    )
    expire_time = models.DateTimeField(
        verbose_name='라이센스 만료 시각',
    )
    last_active_time = models.DateTimeField(
        verbose_name='최근 로그인 시각',
        null=True,
        blank=True,
    )
    local_max_count = models.PositiveIntegerField(
        verbose_name='오프라인 시 최대 사용 가능 횟수',
        default=20,
    )

    for_test = models.BooleanField(
        verbose_name='테스트용 라이센스',
        default=False,
    )
    disabled = models.BooleanField(
        verbose_name='사용 중지',
        default=False,
    )
    purchased_apps = models.ManyToManyField(
        verbose_name='구매한 앱',
        to=App,
        related_name='available_licenses',
        blank=True,
    )
    purchased_contents = models.ManyToManyField(
        verbose_name='구매한 콘텐츠',
        to=Content,
        related_name='available_licenses',
        blank=True,
    )
    institution = models.ForeignKey(
        verbose_name='기관',
        to=Institution,
        on_delete=models.SET_NULL,
        related_name='licenses',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = '라이센스'
        verbose_name_plural = '라이센스'

    def __str__(self):
        return self.description

    def is_active(self):
        return self.expire_time >= now() and not self.disabled

    def available_apps(self):
        if self.is_active():
            return self.purchased_apps
        return []

    def available_contents(self):
        if self.is_active():
            return self.purchased_contents.filter(app__in=self.purchased_apps.all())
        return []

    is_active.boolean = True
    is_active.short_description = '활성화'
