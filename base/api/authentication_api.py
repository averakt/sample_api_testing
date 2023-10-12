from http import HTTPStatus
from functools import lru_cache

from httpx import Client, Response

from models.authentication import AuthUser
from settings import base_settings
from utils.constants.routes import APIRoutes


def get_auth_token_api(payload: AuthUser) -> Response:
    print(payload)
    client = Client(base_url=base_settings.api_url)
    return client.post(f'{APIRoutes.AUTH}',  auth=(payload.email, payload.password))


@lru_cache(maxsize=None)
def get_auth_token(payload: AuthUser) -> str:
    """
    Should be used like this:

    response = get_auth_token_api(payload)
    json_response = response.json()

    assert response.status_code == HTTPStatus.OK
    assert json_response.get('token')

    return json_response['token']
    """
    # return 'token'

    response = get_auth_token_api(payload)
    json_response = response.json()
    print(json_response)
    assert response.status_code == HTTPStatus.OK
    assert json_response.get('token')

    return json_response['token']