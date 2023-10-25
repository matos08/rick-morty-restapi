from datetime import datetime

from faker import Factory
import pytest

faker = Factory.create("pt_BR")


@pytest.fixture()
def character_fake_dict():
    return {
        "id": faker.random_int(min=1, max=999),
        "name": faker.name(),
        "status": faker.name(),
        "species": faker.name(),
        "type": faker.name(),
        "gender": faker.name(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }


@pytest.fixture()
def create_character_fake_dict():
    return {
        "name": faker.name(),
        "status": faker.name(),
        "species": faker.name(),
        "type": faker.name(),
        "gender": faker.name(),
        "location_id": 1,
    }


@pytest.fixture()
def location_fake_dict():
    return {
        "id": faker.random_int(min=1, max=999),
        "name": faker.name(),
        "type": faker.name(),
        "dimension": faker.name(),
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }


@pytest.fixture()
def create_location_fake_dict():
    return {
        "name": faker.name(),
        "type": faker.name(),
        "dimension": faker.name(),
    }
