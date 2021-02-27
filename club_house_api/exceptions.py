"""
:authors: Peopl3s
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2021 Peopl3s
"""

from .enums import *

class ClubHouseError(Exception):
    """ Basic exception when working with the Club House """
    pass

class HttpApiMethodError(ClubHouseError):
    """ HTTP request to API """
    pass

class ApiError(ClubHouseError):
    def __init__(self, error: dict, response_status_code: int) -> None:
        self.code_error = response_status_code
        self.error = error
        super().__init__(self.full_error_discription)
    
    @property
    def message_error(self) -> str:
        print(self.error)
        return str(self.error['message']) + (str(self.error['errors']) if 'errors' in self.error else '')

    @property
    def full_error_discription(self) -> str:
        return '<Code error: {0}, Message: {1}>'.format(self.code_error, self.message_error)
    
    