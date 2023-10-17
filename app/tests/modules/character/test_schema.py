from datetime import datetime

from fastapi_camelcase import CamelModel

from app.modules.character import schemas


def test_character_schema(character_fake_dict):
    character = schemas.CharacterSchema(**character_fake_dict)
    assert isinstance(character, CamelModel)
    assert isinstance(character.id, int)
    assert isinstance(character.name, str)
    assert isinstance(character.status, str)
    assert isinstance(character.species, str)
    assert isinstance(character.type, str)
    assert isinstance(character.gender, str)
    assert isinstance(character.created_at, datetime)
    assert isinstance(character.updated_at, datetime)


def test_create_character_schema(character_fake_dict):
    character = schemas.CreateCharacterSchema(**character_fake_dict)
    assert isinstance(character, CamelModel)
    assert isinstance(character.name, str)
    assert isinstance(character.status, str)
    assert isinstance(character.species, str)
    assert isinstance(character.type, str)
    assert isinstance(character.gender, str)


def test_update_character_schema(character_fake_dict):
    character = schemas.UpdateCharacterSchema(**character_fake_dict)
    assert isinstance(character, CamelModel)
    assert isinstance(character.name, str)
    assert isinstance(character.status, str)
    assert isinstance(character.type, str)
