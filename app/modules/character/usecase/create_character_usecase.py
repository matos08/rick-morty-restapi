from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.character import schemas
from app.modules.character.model import CharacterModel
from app.modules.character.repository import CharacterRepository
from fastapi import HTTPException, status


class CreateCharacterUseCase:
    def __init__(self, payload: schemas.CreateCharacterSchema):
        self._payload = payload
        self._repository = CharacterRepository()
        self._pydantic_model = pydantic_model_creator(CharacterModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        character = await self._repository.get_or_none(
            name=self._payload.name, gender=self._payload.gender
        )
        if character:
            raise HTTPException(
                detail="Character already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.CharacterSchema:
        await self.validate()
        character = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(character)
        return schemas.CharacterSchema(**pyd_model.dict())
