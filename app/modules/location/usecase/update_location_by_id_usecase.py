from fastapi import HTTPException, status

from app.modules.location import schemas
from app.modules.location.repository import LocationRepository


class UpdateLocationById:
    """
    Create for a location by id in the database
    """

    def __init__(self, id: int, payload: schemas.UpdateLocationSchema):
        self._id = id
        self._payload = payload
        self._repository = LocationRepository()

    async def validate(self):
        """
        Search and validate existing location in the database by id
        :return: model location
        """
        location = await self._repository.get_or_none(id=self._id)

        if not location:
            raise HTTPException(
                detail="Location not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return location

    async def execute(self) -> schemas.LocationSchema:
        await self.validate()
        location = await self._repository.update(self._id, **self._payload.dict())
        return schemas.LocationSchema.from_orm(location)
