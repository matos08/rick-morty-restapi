from fastapi_camelcase import CamelModel


class CreateCharacterSchema(CamelModel):
    """
    Schema for create new character.
    """

    name: str
    status: str
    species: str
    type: str
    gender: str
