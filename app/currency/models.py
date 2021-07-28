from django.db import models


# Model
class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # examples: privatbank, monobank
    type = models.CharField(max_length=3)  # noqa


class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=2056)
    created = models.DateTimeField(auto_now_add=True)
