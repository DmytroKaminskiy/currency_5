from rest_framework import generics
from rest_framework import viewsets

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework.response import Response

from api.v1.filters import RateFilter
from api.v1.paginators import RatePagination
from api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from api.v1.throttles import AnonUserRateThrottle
from currency.models import Rate, Source, ContactUs
from currency import model_choices as mch
from currency.tasks import contact_us


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


class SourceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    ordering_fields = ['id', 'email_to']
    filterset_fields = ['email_to', ]
    search_fields = ['email_to']

    def perform_create(self, serializer):
        super().perform_create(serializer)
        subject = serializer.data['subject']
        body = serializer.data['body']
        email_to = serializer.data['email_to']

        full_email_body = f'''
                Email From: {email_to}
                Body: {body}
                '''
        contact_us.apply_async(args=(subject, full_email_body))