from datetime import datetime

from tortoise import Model

from app.modules.character.model import CharacterModel


def test_character_model(character_fake_dict):
    character = CharacterModel(**character_fake_dict)
    assert isinstance(character, Model)
    assert isinstance(character.id, int)
    assert isinstance(character.name, str)
    assert isinstance(character.status, str)
    assert isinstance(character.species, str)
    assert isinstance(character.type, str)
    assert isinstance(character.gender, str)
    assert isinstance(character.created_at, datetime)
    assert isinstance(character.updated_at, datetime)
