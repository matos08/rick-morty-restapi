from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.location import schemas, usecase

router = APIRouter()


@router.post(
    "/location/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.LocationSchema,
)
async def create_location(payload: schemas.CreateLocationSchema):
    result = await usecase.CreateLocationUseCase(payload).execute()
    return result


@router.get(
    "/location/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.LocationSchema,
)
async def get_location_by_id(id: int):
    result = await usecase.GetLocationById(id).execute()
    return result


@router.delete(
    "/location/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_location_by_id(id: int):
    result = await usecase.DeleteLocationById(id).execute()
    return result


@router.put(
    "/location/{id}",
    response_model=schemas.LocationSchema,
    status_code=status.HTTP_200_OK,
)
async def update_location_by_id(id: int, payload: schemas.UpdateLocationSchema):
    result = await usecase.UpdateLocationById(id, payload).execute()
    return result
