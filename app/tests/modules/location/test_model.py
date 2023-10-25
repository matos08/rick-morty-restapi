from datetime import datetime

from tortoise import Model

from app.modules.location.model import LocationModel


def test_location_model(location_fake_dict):
    location = LocationModel(**location_fake_dict)
    assert isinstance(location, Model)
    assert isinstance(location.id, int)
    assert isinstance(location.name, str)
    assert isinstance(location.type, str)
    assert isinstance(location.dimension, str)
    assert isinstance(location.created_at, datetime)
    assert isinstance(location.updated_at, datetime)
