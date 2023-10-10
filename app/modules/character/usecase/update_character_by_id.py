from fastapi import HTTPException, status

from app.modules.character import schemas
from app.modules.character.repository import CharacterRepository


class UpdateCharacterById:
    """
    Create for a character by id in the database
    """

    def __init__(self, id: int, payload: schemas.UpdateCharacterSchema):
        self._id = id
        self._payload = payload
        self._repository = CharacterRepository()

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
        await self.validate()
        character = await self._repository.update(self._id, **self._payload.dict())
        return schemas.CharacterSchema.from_orm(character)
