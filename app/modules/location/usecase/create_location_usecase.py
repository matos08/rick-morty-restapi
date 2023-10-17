from app.modules.location import schemas
from app.modules.location.repository import LocationRepository
from fastapi import HTTPException, status


class CreateLocationUseCase:
    def __init__(self, payload: schemas.CreateLocationSchema):
        self._payload = payload
        self._repository = LocationRepository()

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        location = await self._repository.get_or_none(
            name=self._payload.name, dimension=self._payload.dimension
        )
        if location:
            raise HTTPException(
                detail="location already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.LocationSchema:
        await self.validate()
        location = await self._repository.create(self._payload.dict())
        return schemas.LocationSchema.from_orm(location)
