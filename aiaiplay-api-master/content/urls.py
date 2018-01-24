from django.urls import re_path

from .views import \
    AppList, \
    AppDetail, \
    ContentList,\
    ContentDetail,\
    LauncherVersionDetail, \
    LatestLauncherVersionDetail, \
    ContentVersionDetail, \
    LatestContentVersionDetail

urlpatterns = [
    re_path('apps/$', AppList.as_view()),
    re_path('apps/(?P<id>\d+)/', AppDetail.as_view()),
    re_path('contents/$', ContentList.as_view()),
    re_path('contents/(?P<id>\d+)/', ContentDetail.as_view()),
    re_path('versions/launcher/latest/', LatestLauncherVersionDetail.as_view()),
    re_path('versions/launcher/(?P<version_number>[\w.]+)/', LauncherVersionDetail.as_view()),
    re_path('versions/(?P<content_id>\d+)/latest/', LatestContentVersionDetail.as_view()),
    re_path('versions/(?P<content_id>\d+)/(?P<version_number>[\w.]+)/', ContentVersionDetail.as_view()),
]
