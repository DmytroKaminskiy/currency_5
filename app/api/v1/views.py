from rest_framework import generics
from rest_framework import viewsets

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework.response import Response

from api.v1.filters import RateFilter
from api.v1.paginators import RatePagination
from api.v1.serializers import RateSerializer
from api.v1.throttles import AnonUserRateThrottle
from currency.models import Rate
from currency import model_choices as mch


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonUserRateThrottle]


class RateChoicesView(generics.GenericAPIView):
    def get(self, request):
        return Response(
            {'rate_types': mch.RATE_TYPES},
        )
