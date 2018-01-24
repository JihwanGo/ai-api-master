from django.contrib import admin

from .models import App, Content, LauncherVersion, ContentVersion


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'num_distributions',
    )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'scene_name',
        'num_distributions',
        'asset_bundle_name',
    )


@admin.register(LauncherVersion)
class LauncherVersionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'update_time',
        'download_url',
    )


@admin.register(ContentVersion)
class ContentVersionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'update_time',
        'download_url',
        'minimum_launcher_version',
        'asset_bundle_number',
    )
