from app.modules.character import schemas, repository
from app.modules.character.repository import CharacterRepository
from fastapi import HTTPException, status


class CreateCharacterUseCase:
    def __init__(self, payload: schemas.CreateCharacterSchema):
        self._payload = payload
        self._repository = CharacterRepository()

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
        return schemas.CharacterSchema.from_orm(character)
