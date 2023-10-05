from app.modules.character.model import CharacterModel


class CharacterRepository:
    """
    Class responsible for performing actions on the database
    """

    def __init__(self):
        self.entity = CharacterModel

    async def create(self, data: dict):
        return await self.entity.create(**data)

    async def get_or_none(self, **kwargs):
        return await self.entity.filter(**kwargs).first()
    