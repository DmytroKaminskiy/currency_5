from rest_framework.test import APIClient

from currency.models import Source


def test_get_rates():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()


def test_post_invalid():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.post(url, json={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_post_valid():
    client = APIClient()
    source = Source.objects.last()
    url = '/api/v1/rates/'
    json_data = {
        'buy': 21,
        'sale': 22,
        'source': source.pk,
    }
    response = client.post(url, data=json_data)
    assert response.status_code == 201
    assert response.json()['buy'] == '21.00'
    assert response.json()['sale'] == '22.00'
    assert response.json()['type'] == 'USD'
