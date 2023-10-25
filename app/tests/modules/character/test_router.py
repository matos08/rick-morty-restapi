from fastapi import status

END_POINT = "/character/"
END_POINT_LOCATION = "/location/"


def test_router_create_character_should_be_return_201(
    test_app, create_character_fake_dict, create_location_fake_dict
):
    response_location = test_app.post(
        END_POINT_LOCATION, json=create_location_fake_dict
    )
    assert response_location.status_code == status.HTTP_201_CREATED
    data = response_location.json()
    create_character_fake_dict["location_id"] = data.get("id")
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    print(response.text)
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


def test_router_delete_character_by_id_should_be_return_200(
    test_app, create_character_fake_dict
):
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    deleted_character = response.json()
    response = test_app.delete(f"{END_POINT}{deleted_character['id']}")
    assert response.status_code == status.HTTP_200_OK


def test_router_delete_character_by_id_should_be_return_400(
    test_app, create_character_fake_dict
):
    response = test_app.delete(f"{END_POINT}{9999}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_router_update_character_by_id_should_be_return_200(
    test_app, create_character_fake_dict
):
    response = test_app.post(END_POINT, json=create_character_fake_dict)
    assert response.status_code == status.HTTP_201_CREATED
    update_character = response.json()
    data = {"name": "Rick", "status": "Dead", "type": "Rick's Toxic Side"}
    response = test_app.put(f"{END_POINT}{update_character['id']}", json=data)
    assert response.status_code == status.HTTP_200_OK


def test_router_update_character_by_id_should_be_return_400(
    test_app, create_character_fake_dict
):
    data = {"name": "Rick", "status": "Dead", "type": "Rick's Toxic Side"}
    response = test_app.put(f"{END_POINT}{9999}", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
