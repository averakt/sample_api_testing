import allure
from httpx import Response

from base.client import get_client
from models.authentication import Authentication
from models.users import ModelUserReqBody, ModelUser, User
from models.accounts import (AccountClass, ModelAccount, AccountReqBodyClass, ModelAccountReqBody)
from utils.constants.routes import APIRoutes


@allure.step(f'Getting all questions')
def get_users_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    # print("client.headers:", client.headers)
    return client.get(APIRoutes.USERS)


@allure.step(f'Getting user')
def get_user_api(
        user_id: int,
        # payload: ModelAccountBody,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    # print("client.headers:", client.headers)
    return client.get(f'{APIRoutes.USERS}/{user_id}')


@allure.step(f'Getting account')
def get_account_api(
        account_id: int,
        # payload: ModelAccountBody,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    # print("client.headers:", client.headers)
    return client.get(f'{APIRoutes.ACCOUNT}/{account_id}')


@allure.step(f'Add new account')
def add_account_api(
        payload: ModelAccountReqBody,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.ACCOUNT, json=payload.dict(by_alias=True))


@allure.step(f'Add new user')
def add_user_api(
        payload: ModelUserReqBody,
        auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.USERS, json=payload.dict(by_alias=True))


@allure.step(f'Update user')
def update_user_api(
        user_id: int,
        payload: ModelUserReqBody,
        auth: Authentication = Authentication()
) -> Response:
    # print("payload", payload.dict())
    # print("user_id", user_id)
    client = get_client(auth=auth)
    return client.put(f'{APIRoutes.USERS}/{user_id}', json=payload.dict(by_alias=True))


@allure.step(f'Update account')
def update_account_api(
        account_id: int,
        payload: ModelAccount,
        auth: Authentication = Authentication()
) -> Response:
    # print("payload", payload.dict())
    # print("account_id", account_id)
    client = get_client(auth=auth)
    return client.put(f'{APIRoutes.ACCOUNT}/{account_id}', json=payload.dict(by_alias=True))


@allure.step('Deleting user with id "{user_id}"')
def delete_user_api(
    user_id: int,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.delete(f'{APIRoutes.USERS}/{user_id}')


@allure.step('Deleting account with id "{account_id}"')
def delete_account_api(
    account_id: int,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.delete(f'{APIRoutes.ACCOUNT}/{account_id}')


def create_user(auth: Authentication = Authentication()) -> User:
    payload = ModelUserReqBody()

    response = add_user_api(payload=payload, auth=auth)
    # print("response_create_user:", response.json())
    # return ModelUser(**response.json())
    return User(**response.json())


def create_account(auth: Authentication = Authentication()) -> AccountClass:
    payload = ModelAccountReqBody()
    # print(payload)
    response = add_account_api(payload=payload, auth=auth)
    # print("response_create_account:", response.json())
    # return ModelUser(**response.json())
    return AccountClass(**response.json())


