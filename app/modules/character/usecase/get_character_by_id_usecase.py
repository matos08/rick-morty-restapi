from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.character import schemas
from app.modules.character.model import CharacterModel
from app.modules.character.repository import CharacterRepository


class GetCharacterById:
    """
    Search for a character by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CharacterRepository()
        self._pydantic_model = pydantic_model_creator(CharacterModel)

    async def validate(self):
        """
        Search and validate existing characters in the database by id
        :return: model character
        """
        character = await self._repository.get_or_none(id=self._id)

        if not character:
            raise HTTPException(
                detail="Character not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return character

    async def execute(self) -> schemas.CharacterSchema:
        character = await self.validate()
        pyd_model = await self._pydantic_model.from_tortoise_orm(character)
        return schemas.CharacterSchema(**pyd_model.dict())
