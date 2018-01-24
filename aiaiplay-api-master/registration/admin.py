from django.contrib import admin

from .models import User, Institution, License

admin.site.site_header = 'aiaiPlay 관리자'
admin.site.site_title = 'aiaiPlay'
admin.site.index_title = '데이터 관리'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'num_licenses',
    )


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'key',
        'institution',
        'is_active',
        'for_test',
    )
