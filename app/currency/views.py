from django.urls import reverse_lazy
from urllib.parse import urlencode

from currency.filters import RateFilter
from currency.services import get_latest_rates
from currency.tasks import contact_us

from currency.utils import generate_password as gen_pass
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView,
    DeleteView, TemplateView
)

from django_filters.views import FilterView

from django.http import HttpResponse


class GeneratePasswordView(TemplateView):
    template_name = 'generate_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        password_len = int(self.request.GET.get('password-len'))
        context['password'] = gen_pass(password_len)

        return context


class RateListView(FilterView):
    queryset = Rate.objects.all().defer('created').select_related('source').order_by('-created')
    template_name = 'rate_list.html'
    paginate_by = 25
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        get_parameters = {}
        for key, value in self.request.GET.items():
            if key != 'page':
                get_parameters[key] = value

        context['pagination_params'] = urlencode(get_parameters)

        return context


class RateCreateView(CreateView):
    # model = Rate
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'contactus_create.html'
    fields = (
        'email_to',
        'subject',
        'body',
    )

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        email_to = form.cleaned_data['email_to']

        full_email_body = f'''
        Email From: {email_to}
        Body: {body}
        '''
        contact_us.apply_async(args=(subject, full_email_body))

        return super().form_valid(form)

class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceListView(ListView):
    # queryset = Source.objects.all().prefetch_related('rates')
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class LatestRatesView(TemplateView):
    template_name = 'latest_rates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_list'] = get_latest_rates()
        return context

# def rates_list_api_example(request):
#     import json
#
#     rates = Rate.objects.all()
#     result = []
#     for rate in rates:
#         result.append({
#             'id': rate.id,
#             'buy': float(rate.buy),
#             'sale': float(rate.sale),
#         })
#
#     # return HttpResponse(json.dumps(result), content_type='application/json')
#     return JsonResponse(result, safe=False)


def response_codes(request):
    '''
    Informational
    1xx
    101 - connected

    Success
    2xx
    200 - Ok
    201 - Created
    202 - Accepted

    Redirect
    3xx
    301 - Permanent
    302 - temporary

    Client Errors
    4xx
    400 - Bad Request
    404 - Not Found (page, resource, object)

    Server Error
    5xx
    500 - Server Error
    502 - server not available
    '''
    from time import sleep
    sleep(5)

    response = HttpResponse('Status Code', status=404)
    return response
