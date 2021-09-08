from currency.views import (
    GeneratePasswordView,
    RateListView, response_codes, RateCreateView,
    RateDetailView, RateUpdateView,
    RateDeleteView, ContactUsCreateView,
    SourceDetailView,
    # rates_list_api_example,
)
from django.urls import path

app_name = 'currency'

urlpatterns = [
    # currency
    # path('rate/list/', rate_list),
    # path('rate/create/', rate_create, name='rate-create'),
    # path('rate/details/<int:rate_id>/', rate_details),
    # path('rate/update/<int:rate_id>/', rate_update),
    # path('rate/delete/<int:rate_id>/', rate_delete),

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),

    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),

    path('response-codes/', response_codes),
    path('gen-pass/', GeneratePasswordView.as_view()),

    # API example
    # path('api/rate/list/', rates_list_api_example),
]
