from fastapi import HTTPException, status

from app.modules.character import schemas
from app.modules.character.repository import CharacterRepository


class DeleteCharacterById:
    """
    Delete for a character by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CharacterRepository()

    async def validate(self):
        """
        Search and validate existing characters in the database by id
        :return: model character
        """
        character = await self._repository.get_or_none(id=self._id)

        if not character:
            raise HTTPException(
                detail="Character not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return character

    async def execute(self) -> schemas.DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return schemas.DefaultSchema(detail="Character deleted successfully")
