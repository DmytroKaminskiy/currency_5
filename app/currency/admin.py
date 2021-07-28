from django.contrib import admin
from currency.models import Rate

from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin

from currency.resources import RateResource


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        'source',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'type',
        'source',
    )
    readonly_fields = (
        'sale',
        'buy',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
