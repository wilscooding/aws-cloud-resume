import requests


def test_get_count_endpoint():
    url = 'https://yfniwvuig9.execute-api.us-east-1.amazonaws.com/Prod/get'
    response = requests.get(url)

    # Check status code
    assert response.status_code == 200

    # Check response body content
    data = response.json()
    assert 'count' in data
    assert isinstance(data['count'], int)
