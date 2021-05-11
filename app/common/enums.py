from enum import IntEnum

class ErrorCodes(IntEnum):
    SUCCESS = 0
    TYPE = 1
    SCHEMA = 2
    UNKNOWN_USER = 3
    INCORRECT_PASSWORD = 4

class HTTPStatusCodes(IntEnum):
    OK = 200
    UNAUTHORIZED = 401