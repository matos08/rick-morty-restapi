from datetime import datetime

from fastapi_camelcase import CamelModel

from app.modules.location import schemas


def test_location_schema(location_fake_dict):
    location = schemas.LocationSchema(**location_fake_dict)
    assert isinstance(location, CamelModel)
    assert isinstance(location.id, int)
    assert isinstance(location.name, str)
    assert isinstance(location.type, str)
    assert isinstance(location.dimension, str)
    assert isinstance(location.created_at, datetime)
    assert isinstance(location.updated_at, datetime)


def test_create_location_schema(location_fake_dict):
    location = schemas.CreateLocationSchema(**location_fake_dict)
    assert isinstance(location, CamelModel)
    assert isinstance(location.name, str)
    assert isinstance(location.type, str)
    assert isinstance(location.dimension, str)


def test_update_location_schema(location_fake_dict):
    location = schemas.UpdateLocationSchema(**location_fake_dict)
    assert isinstance(location, CamelModel)
    assert isinstance(location.name, str)
    assert isinstance(location.type, str)
    assert isinstance(location.dimension, str)
