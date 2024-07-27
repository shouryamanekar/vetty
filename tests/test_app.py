import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_list_coins(client):
    response = client.get('/coins')
    assert response.status_code == 200


def test_list_categories(client):
    response = client.get('/categories')
    assert response.status_code == 200


def test_get_coin(client):
    response = client.get('/coins/bitcoin')
    assert response.status_code == 200
