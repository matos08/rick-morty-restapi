from fastapi import status

END_POINT = "/character/"


def test_router_create_character_should_be_return_201(
    test_app, create_character_fake_dict
):
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED


def test_router_create_character_should_be_return_400(
    test_app, create_character_fake_dict
):
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED

    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_router_get_character_by_id_should_be_return_200(
    test_app, create_character_fake_dict
):
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    created_character = response.json()
    response = test_app.get(f"{END_POINT}{created_character.get('id')}")
    assert response.status_code == status.HTTP_200_OK


def test_router_get_character_by_id_should_be_return_400(
    test_app, create_character_fake_dict
):
    response = test_app.get(f"{END_POINT}{9999}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
