from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import App, Content, LauncherVersion
from .serializers import \
    AppSerializer, \
    SimpleAppSerializer, \
    ContentSerializer, \
    SimpleContentSerializer, \
    LauncherVersionSerializer, \
    ContentVersionSerializer


class AppList(ListAPIView):
    serializer_class = SimpleAppSerializer
    queryset = App.objects.all()


class AppDetail(RetrieveAPIView):
    serializer_class = AppSerializer
    queryset = App.objects.all()
    lookup_field = 'id'


class ContentList(ListAPIView):
    serializer_class = SimpleContentSerializer
    queryset = Content.objects.all()


class ContentDetail(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_field = 'id'


class LauncherVersionDetail(RetrieveAPIView):
    serializer_class = LauncherVersionSerializer
    queryset = LauncherVersion.objects.all()
    lookup_field = 'version_number'


class LatestLauncherVersionDetail(LauncherVersionDetail):
    def get_object(self):
        return LauncherVersion.objects.latest('update_time')


class ContentVersionDetail(RetrieveAPIView):
    serializer_class = ContentVersionSerializer
    lookup_field = 'version_number'

    def get_queryset(self):
        content_id = self.kwargs.get('content_id')
        content = get_object_or_404(Content, id=content_id)
        return content.versions.all()


class LatestContentVersionDetail(ContentVersionDetail):
    def get_object(self):
        return self.get_queryset().latest('update_time')
