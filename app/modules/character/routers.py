from fastapi import APIRouter, status

from app.modules.character import schemas, usecase
from app.modules.core.default_schema import DefaultSchema

router = APIRouter()


@router.post(
    "/character/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CharacterSchema,
)
async def create_character(payload: schemas.CreateCharacterSchema):
    result = await usecase.CreateCharacterUseCase(payload).execute()
    return result


@router.get(
    "/character/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.CharacterSchema,
)
async def get_character_by_id(id: int):
    result = await usecase.GetCharacterById(id).execute()
    return result


@router.delete(
    "/character/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_character_by_id(id: int):
    result = await usecase.DeleteCharacterById(id).execute()
    return result


@router.put(
    "/character/{id}",
    response_model=schemas.CharacterSchema,
    status_code=status.HTTP_200_OK,
)
async def update_character_by_id(id: int, payload: schemas.UpdateCharacterSchema):
    result = await usecase.UpdateCharacterById(id, payload).execute()
    return result
