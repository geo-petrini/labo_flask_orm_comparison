# Tortoise ORM + aerich Example
# Note: Tortoise is an async ORM, typically used with FastAPI/Quart
# This example shows the model definition and migration setup

from tortoise import fields, models
from tortoise.validators import RegexValidator


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=80, unique=True)
    email = fields.CharField(max_length=120, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user"

    def __str__(self):
        return self.username


# aerich configuration (aerich.ini)
# [aerich]
# tortoise_orm = app TORTOISE_ORM
# location = ./migrations

# TORTOISE_ORM = {
#     "connections": {
#         "default": "sqlite://tortoise_app.db"
#     },
#     "apps": {
#         "models": {
#             "models": ["app"],
#             "default_connection": "default",
#         }
#     }
# }
