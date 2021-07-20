"""Enums"""

from enum import IntEnum


class ErrorCodes(IntEnum):
    """Error code enums"""
    SUCCESS = 0
    TYPE = 1
    SCHEMA = 2
    UNKNOWN_USER = 3
    INCORRECT_PASSWORD = 4
    UNKNOWN_METHOD = 5
    ATTRIB_ERROR = 6
    VALUE_ERROR = 7

class HTTPStatusCodes(IntEnum):
    """HTTP status enums"""
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
