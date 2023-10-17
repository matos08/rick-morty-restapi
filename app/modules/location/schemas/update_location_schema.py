from fastapi_camelcase import CamelModel


class UpdateLocationSchema(CamelModel):
    """
    Schema for update a location.
    """

    name: str
    type: str
    dimension: str
