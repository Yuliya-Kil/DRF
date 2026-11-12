import django_filters
from .models import Advertisement

class AdvertisementFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
