from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView

from .models import License
from .serializers import LicenseSerializer


class LicenseDetail(RetrieveAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()

    def get_object(self):
        key = self.kwargs.get('key')
        unity_key = self.request.query_params.get('unity_key', None)
        if unity_key is None:
            raise NotFound(detail='Unity 키를 입력하세요.')

        license = get_object_or_404(License, key=key)
        if license.register_time:
            if license.unity_key != unity_key:
                raise NotFound(detail='이미 사용된 라이센스입니다.')
        else:
            license.unity_key = unity_key
            license.register_time = now()
            license.save()

        return license
