from django.db import models
from currency import model_choices as mch


# Model
class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # examples: privatbank, monobank
    type = models.CharField(max_length=3, choices=mch.RATE_TYPES)  # noqa
    # .get_{filed_name}_display()



class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=2056)
    created = models.DateTimeField(auto_now_add=True)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    response_time = models.PositiveSmallIntegerField(
        help_text='in milliseconds.'
    )
    # request_method = ('GET', 'POST') - choices
