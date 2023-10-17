from fastapi import HTTPException, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.location import schemas
from app.modules.location.repository import LocationRepository


class DeleteLocationById:
    """
    Delete for a location by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = LocationRepository()

    async def validate(self):
        """
        Search and validate existing location in the database by id
        :return: model location
        """
        location = await self._repository.get_or_none(id=self._id)

        if not location:
            raise HTTPException(
                detail="Location not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return location

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Location deleted successfully")
