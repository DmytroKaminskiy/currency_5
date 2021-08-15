from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import requests
from decimal import Decimal
from currency import model_choices as mch


def round_currency(num):
    return Decimal(num).quantize(Decimal('.01'))


@shared_task
def debug_task(sleep_time: int = 5):
    from currency.models import Rate
    print(f'Count Rates: {Rate.objects.count()}')

    # print('Starting Debug')
    # from time import sleep
    # sleep(sleep_time)
    # print(f'Task completed in {sleep_time}')


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Rate

    privatbank_currency_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(privatbank_currency_url)

    response.raise_for_status()  # raise error if status_code is not 2xx

    rates = response.json()
    source = 'privatbank'
    # available_currency_types = ('USD', 'EUR')
    available_currency_types = {
        'USD': mch.TYPE_USD,
        'EUR': mch.TYPE_EUR,
    }

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:

            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])
            ct = available_currency_types[currency_type]

            last_rate = Rate.objects.filter(
                type=ct,
                source=source,
            ).order_by('created').last()  # last() - returns object or None

            if (
                    last_rate is None or  # first attempt to parse (last rate does not exists)
                    last_rate.sale != sale or # last sale was changed
                    last_rate.buy != buy # last buy was changed
            ):
                Rate.objects.create(
                    type=ct,
                    sale=sale,
                    buy=buy,
                    source=source,
                )
