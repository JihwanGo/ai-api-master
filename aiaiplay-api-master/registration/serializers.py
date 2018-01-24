from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import License


class LicenseSerializer(HyperlinkedModelSerializer):
    institution_name = serializers.SerializerMethodField()
    available_apps = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    available_contents = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = License
        fields = (
            'unity_key',
            'institution_name',
            'is_active',
            'expire_time',
            'local_max_count',
            'available_apps',
            'available_contents',
        )

    def get_institution_name(self, obj):
        if obj.institution:
            return obj.institution.name
        return ''
