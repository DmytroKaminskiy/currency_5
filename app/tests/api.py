from currency.models import Source


def test_get_rates(api_client_auth):
    print('START TEST')
    url = '/api/v1/rates/'
    response = api_client_auth.get(url)
    assert response.status_code == 200
    assert response.json()
    print('END TEST')


def test_post_invalid(api_client_auth):
    url = '/api/v1/rates/'
    response = api_client_auth.post(url, json={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.'],
    }


def test_post_valid(api_client_auth):
    source = Source.objects.last()
    url = '/api/v1/rates/'
    json_data = {
        'buy': 21,
        'sale': 22,
        'source': source.pk,
    }
    response = api_client_auth.post(url, data=json_data)
    assert response.status_code == 201
    assert response.json()['buy'] == '21.00'
    assert response.json()['sale'] == '22.00'
    assert response.json()['type'] == 'USD'
