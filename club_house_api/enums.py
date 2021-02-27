"""
:authors: Peopl3s
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2021 Peopl3s
"""

from enum import IntEnum, Enum, auto

class HttpRequestTypes(IntEnum):
    """ Enum the types of HTTP requests """
    GET = auto()

    POST = auto()

    PUT = auto()

    DELETE = auto()

    BAD_TYPE = auto()

class ResponseCodes(Enum):
    """ Status codes response to the HTTP request """
    OK = (200, 201)

    SCHEMA_MISMATCH = 400

    RESOURCE_DOES_NOT_EXIST = 404

    UNPROCESSIBLE = 422

    NO_CONTENT = 204

    TOO_MATCH_REQUEST = 429 




    
