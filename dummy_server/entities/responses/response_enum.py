from enum import Enum

class ResponseState(str, Enum):
    success = 'success'
    failed = 'failed'

class OperationFailCode(str, Enum):
    authorization_failed = 'authorization_failed'
    undefined = 'undefined'
