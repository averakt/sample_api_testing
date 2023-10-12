from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/api/v1/tokens'
    USERS = 'api/v1/users'
    ACCOUNT = '/api/v1/accounts'

    def __str__(self) -> str:
        return self.value
