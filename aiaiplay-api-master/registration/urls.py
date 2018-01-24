from django.urls import re_path

from .views import LicenseDetail

urlpatterns = [
    re_path('licenses/(?P<key>\w+)/', LicenseDetail.as_view()),
]
