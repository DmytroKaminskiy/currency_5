from django.db import models
from django.templatetags.static import static

from currency import model_choices as mch


class Source(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=24, unique=True, editable=False)

    logo = models.FileField(
        upload_to=f'sources/logo',
        blank=True,
        null=True,
        default=None,
    )

    # .get_{filed_name}_display()

    def get_logo(self):
        if self.logo:
            return self.logo.url
        return static('images/source-default.png')


# Model
class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(
        Source,
        related_name='rates',
        on_delete=models.CASCADE,
    )   # source_id
    type = models.CharField(
        max_length=3,
        choices=mch.RATE_TYPES,
        blank=False,
        null=False,
        default=mch.TYPE_USD,
    )


class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=2056)
    created = models.DateTimeField(auto_now_add=True)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255, choices=mch.METHODS, default='GET')
    response_time = models.PositiveSmallIntegerField(
        help_text='in milliseconds.'
    )
    # request_method = ('GET', 'POST') - choices

'''
Customers
id    |    name
1     |    Dmytro Kaminskyi
2     |    Alex R

Orders
id    |    ProductName    |     CustomerId (integer)
1     |    Laptop         |     1
2     |    TV             |     1

=========================================

user
id   | name
1    | Dmytro K
2    | Alex R
3    | Nikolay H

books
id   |   name    |   user_id (int)
1    |   LOTR    |     1
4    |   CCCCCCC |     1
5    |   DDDDDDD |     2
6    |   EEEEEEE |     null



Rate
id  |  buy   |   sale   |   source_id
1   |  23    |   24    |       1
2   |  24    |   25    |       1
3   |  25    |   26    |       1
4   |  25    |   26    |       2

Source
id   |  name
1    |  privatbank
2    |  monobank

OneToOne
OneToMany
ManyToMany
'''