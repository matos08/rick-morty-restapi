from tortoise import Model
from tortoise import fields


class LocationModel(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=50)
    type = fields.CharField(max_length=50)
    dimension = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "location"
        ordering = ["id"]
