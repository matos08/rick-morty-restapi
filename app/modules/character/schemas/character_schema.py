from datetime import datetime

from fastapi_camelcase import CamelModel


class CharacterSchema(CamelModel):
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
