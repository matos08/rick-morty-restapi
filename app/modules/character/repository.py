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
        """
        Objective to filter the first item found in the database
        :param kwargs: Attributes followed by key and value
        exemple: id = 1
        :return:
        """
        return await self.entity.filter(**kwargs).first()

    async def delete(self, **kwargs):
        """
        Objective to delete the items found in the database
        :param kwargs: Attributes followed by key and value
        exemple: id = 1
        :return:
        """
        return await self.entity.delete(**kwargs)
