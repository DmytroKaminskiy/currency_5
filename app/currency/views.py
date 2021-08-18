from django.urls import reverse_lazy
from currency.tasks import contact_us

from currency.utils import generate_password as gen_pass
from currency.models import Rate, ContactUs
from currency.forms import RateForm
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView,
    DeleteView, TemplateView
)

from django.http import HttpResponse, HttpResponseRedirect, Http404


class GeneratePasswordView(TemplateView):
    template_name = 'generate_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        password_len = int(self.request.GET.get('password-len'))
        context['password'] = gen_pass(password_len)

        return context


class RateListView(ListView):
    queryset = Rate.objects.all().order_by('-created')
    template_name = 'rate_list.html'

    # def get(self, request, *args, **kwargs):
    #     print(request.COOKIES)
    #     return super().get(request, *args, **kwargs)


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
        contact_us.apply_async(args=(subject, ), kwargs={'body': full_email_body})

        return super().form_valid(form)


# def rate_list(request):
#     rates = Rate.objects.all()
#     context = {
#         'rate_list': rates,
#     }
#     return render(request, 'rate_list.html', context=context)


# def rate_create(request):
#
#     '''
#     GET /rate/create/?buy=34&sale=34&source=PrivatBank&type=USD
#     Path: /rate/create/
#     Params: buy=34&sale=34&source=PrivatBank&type=USD
#
#     POST /rate/create/
#     Path: /rate/create/
#
#     buy=34&sale=34&source=PrivatBank&type=USD
#
#     R - GET - read object
#     C - POST - create object
#     U - PUT/PATCH - update object
#     D - DELETE - delete object
#     '''
#
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/rate/list/')
#             # return HttpResponseRedirect(reverse('rate-list'))
#             return redirect('rate-list')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_create.html', context=context)


# def rate_details(request, rate_id):
#     # /rate/details/?rate-id=awdaw
#     # /rate/details/102/
#
#     # try:
#     #     rate = Rate.objects.get(id=rate_id)
#     # except Rate.DoesNotExist as exc:
#     #     raise Http404(exc)
#     rate = get_object_or_404(Rate, id=rate_id)
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_details.html', context=context)


# def rate_update(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'rate_update.html', context=context)

#
# def rate_delete(request, rate_id):
#     rate = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         rate.delete()
#         return HttpResponseRedirect('/rate/list/')
#
#     # if request.method == 'GET'
#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_delete.html', context=context)


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

    response = HttpResponse('Status Code', status=404)
    return response
