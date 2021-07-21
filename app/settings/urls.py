from currency.views import (
    generate_password, index,
    rate_list, response_codes, rate_create,
    rate_details, rate_update,
    rate_delete,
)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    # currency
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('response-codes/', response_codes),
    path('gen-pass/', generate_password),
]
