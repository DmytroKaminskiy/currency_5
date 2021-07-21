from django.shortcuts import render, get_object_or_404

from currency.utils import generate_password as gen_pass
from currency.models import Rate
from currency.forms import RateForm

from django.http import HttpResponse, HttpResponseRedirect, Http404


def index(request):
    return render(request, 'index.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HttpResponse(password)


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rate_list': rates,
    }
    return render(request, 'rate_list.html', context=context)


def rate_create(request):

    '''
    GET /rate/create/?buy=34&sale=34&source=PrivatBank&type=USD
    Path: /rate/create/
    Params: buy=34&sale=34&source=PrivatBank&type=USD

    POST /rate/create/
    Path: /rate/create/

    buy=34&sale=34&source=PrivatBank&type=USD

    R - GET - read object
    C - POST - create object
    U - PUT/PATCH - update object
    D - DELETE - delete object
    '''

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form,
    }
    return render(request, 'rate_create.html', context=context)


def rate_details(request, rate_id):
    # /rate/details/?rate-id=awdaw
    # /rate/details/102/

    # try:
    #     rate = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist as exc:
    #     raise Http404(exc)
    rate = get_object_or_404(Rate, id=rate_id)
    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def rate_update(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')

    # if request.method == 'GET'
    context = {
        'object': rate,
    }
    return render(request, 'rate_delete.html', context=context)


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
