from datetime import datetime

from fastapi_camelcase import CamelModel


class LocationSchema(CamelModel):
    id: int
    name: str
    type: str
    dimension: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
