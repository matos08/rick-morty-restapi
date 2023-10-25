from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel

from app.modules.location.schemas import LocationSchema


class CharacterSchema(CamelModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    created_at: datetime
    updated_at: datetime
    location: Optional[LocationSchema]

    class Config:
        orm_mode = True
