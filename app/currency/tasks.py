from celery import shared_task
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
import requests
from decimal import Decimal
from currency import consts
from currency import model_choices as mch
from currency.services import get_latest_rates


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
    # I/O bound
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    # I/O
    from currency.models import Rate, Source

    privatbank_currency_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(privatbank_currency_url)

    response.raise_for_status()  # raise error if status_code is not 2xx

    rates = response.json()
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'name': 'PrivatBank'},
    )[0]
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
                cache.delete(consts.CACHE_KEY_LATEST_RATES)
                get_latest_rates()
