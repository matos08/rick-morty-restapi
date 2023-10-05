from tortoise import Model
from tortoise import fields


class CharacterModel(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=50)
    status = fields.CharField(max_length=50)
    species = fields.CharField(max_length=50)
    type = fields.CharField(max_length=50)
    gender = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "character"
        ordering = ["id"]
