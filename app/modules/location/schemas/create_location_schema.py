from fastapi_camelcase import CamelModel


class CreateLocationSchema(CamelModel):
    """
    Schema for create new location.
    """

    name: str
    type: str
    dimension: str
