

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        if self.action == "create":
            return [IsAuthenticated()]
        return []