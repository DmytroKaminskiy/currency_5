from currency.views import generate_password, index, rate_list, response_codes

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    # currency
    path('rate/list/', rate_list),
    path('response-codes/', response_codes),
    path('gen-pass/', generate_password),
]
