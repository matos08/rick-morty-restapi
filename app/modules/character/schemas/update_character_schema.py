from fastapi_camelcase import CamelModel


class UpdateCharacterSchema(CamelModel):
    """
    Schema for update a character.
    """

    name: str
    status: str
    type: str
