from fastapi import APIRouter
from starlette import status
from app.modules.character import schemas, usecase

router = APIRouter()


@router.post("/character", status_code=status.HTTP_201_CREATED,
             response_model=schemas.CharacterSchema)
async def create_character(payload: schemas.CreateCharacterSchema):
    result = await usecase.CreateCharacterUseCase(payload).execute()
    return result


@router.get("/character/{id}", status_code=status.HTTP_200_OK,
            response_model=schemas.CharacterSchema)
async def get_character_by_id(id: int):
    pass
