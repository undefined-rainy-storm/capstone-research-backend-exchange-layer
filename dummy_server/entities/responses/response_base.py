from flasgger import Schema, fields, validate
from dataclasses import dataclass
from marshmallow.validate import Equal, OneOf
from .response_enum import ResponseState, OperationFailCode

@dataclass
class Response:
    state: ResponseState
    details: str

class ResponseSchema(Schema):
    state = fields.Str(
        required=True,
        validate=OneOf([
            ResponseState.success,
            ResponseState.failed
        ])
    )
    details = fields.Str()

class ResponseOnSuccessSchema(ResponseSchema):
    state = fields.Str(validate=Equal(
        ResponseState.success
    ))

@dataclass
class ResponseOnFailed(Response):
    code: OperationFailCode

class ResponseOnFailedSchema(ResponseSchema):
    state = fields.Str(validate=Equal(
        ResponseState.failed
    ))
    code = fields.Str(validate=OneOf([
        OperationFailCode.authorization_failed,
        OperationFailCode.undefined
    ]))
