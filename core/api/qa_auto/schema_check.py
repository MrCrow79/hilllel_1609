"""
{
  "status": "ok",
  "data": {
    "userId": 1,
    "distanceUnits": "km",
    "currency": "usd",
    "photoFilename": "default-user.png"
  }
}
"""

# pip install marshmallow

from enum import Enum
from marshmallow import Schema, fields, validate, ValidationError, post_load


class DistanceUnits(Enum):
    km = 'km'
    ml = 'ml'

def is_more_than_1(value):
    if value < 1:
        raise ValidationError("Should be more than 0")


def is_not_empty(value):
    if len(value) == 0:
        raise ValidationError("Shouldnt be empty")

validator = validate.And(validate.Range(min=1), is_more_than_1)  # validate.Range(min=1) теж саме, що і is_more_than_1





class UserSchema(Schema):
    user_id = fields.Int(required=True, validate=validator)#, data_key='userId')
    distanceUnits = fields.Enum(enum=DistanceUnits, required=True)
    currency = fields.Str(required=True)
    photoFilename = fields.Str(required=True)
    user_data = fields.List(fields.Str(), validate=is_not_empty)


class CurrentSchema(Schema):
    status = fields.Str(required=True)
    data = fields.Nested(UserSchema, required=True)


    # @post_load
    # def desiralizate(self, data, *args, **kwargs):
    #     return 'Well done'


if __name__ == '__main__':

    user = {
      "status": "ok",
      "data": {
        "userId": 1,
        "distanceUnits": "km",
        "currency": "usd",
        "photoFilename": "default-user.png",
      }
    }

    incorrect_user = {
      "status": "ok",
      "data": {
        "userId": 0,
        "distanceUnits": "km",
        "currency": "usd",
        "photoFilename": "default-user.png",
        "user_data": []
      }
    }


    res = CurrentSchema().load([user, user, user], many=True)
    pass

