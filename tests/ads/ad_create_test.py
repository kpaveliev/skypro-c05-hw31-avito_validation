import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):

    expected_response = {
        "id": 1,
        "image": None,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "author": user.username,
        "category": category.name,
        "is_published": False,
        "description": "Test description"
    }

    data = {
        "author_id": 1,
        "name": "Test 10 characters minimum",
        "price": 2500,
        "description": "Test description",
        "is_published": False,
        "category_id": 1
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
