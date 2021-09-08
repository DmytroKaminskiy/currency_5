import debug_toolbar
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('auth/', include('django.contrib.auth.urls')),

    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/v1/', include('api.v1.urls')),  # 10
    # path('api/v2/', include('api.v2.urls')),  # 9_990
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
