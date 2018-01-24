from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import App, Content, LauncherVersion, ContentVersion


class SimpleAppSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = App
        fields = (
            'id',
            'name',
        )


class SimpleContentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = (
            'id',
            'name',
            'scene_name',
            'asset_bundle_name',
        )


class AppSerializer(HyperlinkedModelSerializer):
    contents = SimpleContentSerializer(many=True)

    class Meta:
        model = App
        fields = (
            'id',
            'name',
            'contents',
        )


class ContentSerializer(HyperlinkedModelSerializer):
    app_name = serializers.CharField(source='app.name')

    class Meta:
        model = Content
        fields = (
            'id',
            'app_name',
            'name',
            'scene_name',
            'asset_bundle_name',
        )


class LauncherVersionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LauncherVersion
        fields = (
            'version_number',
            'download_url',
        )


class ContentVersionSerializer(HyperlinkedModelSerializer):
    minimum_launcher_version = LauncherVersionSerializer()

    class Meta:
        model = ContentVersion
        fields = (
            'version_number',
            'download_url',
            'minimum_launcher_version',
            'asset_bundle_number',
        )
