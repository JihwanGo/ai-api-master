from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'timestamp',
        'type',
        'description',
        'license',
        'launcher_version',
        'content_version',
    )
