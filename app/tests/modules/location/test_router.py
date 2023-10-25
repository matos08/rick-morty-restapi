from fastapi import status

END_POINT = "/location/"


def test_router_create_location_should_be_return_201(
    test_app, create_location_fake_dict
):
    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED


def test_router_create_location_should_be_return_400(
    test_app, create_location_fake_dict
):
    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED

    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_router_get_location_by_id_should_be_return_200(
    test_app, create_location_fake_dict
):
    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    created_character = response.json()
    response = test_app.get(f"{END_POINT}{created_character.get('id')}")
    assert response.status_code == status.HTTP_200_OK


def test_router_get_location_by_id_should_be_return_400(
    test_app, create_location_fake_dict
):
    response = test_app.get(f"{END_POINT}{9999}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_router_delete_location_by_id_should_be_return_200(
    test_app, create_location_fake_dict
):
    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    deleted_location = response.json()
    response = test_app.delete(f"{END_POINT}{deleted_location['id']}")
    assert response.status_code == status.HTTP_200_OK


def test_router_delete_location_by_id_should_be_return_400(
    test_app, create_location_fake_dict
):
    response = test_app.delete(f"{END_POINT}{9999}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_router_update_location_by_id_should_be_return_200(
    test_app, create_location_fake_dict
):
    response = test_app.post(END_POINT, json=create_location_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    update_location = response.json()
    data = {"name": "Rick", "type": "Rick's Toxic Side", "dimension": "Dimension C-137"}
    response = test_app.put(f"{END_POINT}{update_location['id']}", json=data)
    assert response.status_code == status.HTTP_200_OK


def test_router_update_location_by_id_should_be_return_400(
    test_app, create_location_fake_dict
):
    data = {"name": "Rick", "type": "Rick's Toxic Side", "dimension": "Dimension C-137"}
    response = test_app.put(f"{END_POINT}{9999}", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
