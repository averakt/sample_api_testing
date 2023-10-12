from http import HTTPStatus

import allure
import pytest

from base.api.questions_api import (get_users_api, add_user_api, update_user_api, delete_user_api,
                                    get_account_api, get_user_api, add_account_api, delete_account_api,
                                    update_account_api)
# from models.questions import (DefaultUsers)
from models.users import (ModelUserReqBody, User, ModelUser, UserBodyClass)
from models.accounts import (AccountClass, ModelAccount, ModelAccountReqBody)
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.questions
@allure.feature('Minibank')
@allure.story('Minibank API')
class TestMinibank:
    # @allure.title('Get users')
    # def test_get_users(self):
    #     response = get_users_api()
    #     json_response: DefaultUsers = response.json()
    #     assert_status_code(response.status_code, HTTPStatus.OK)
    #     # validate_schema(json_response, DefaultUsers.schema())

    @allure.title('Get user')
    def test_get_user(self):
        response = get_user_api(user_id=1)
        json_response: UserBodyClass = response.json()
        # print(json_response)
        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.title('Update User')
    def test_update_user(self, function_user: ModelUser):
        payload = ModelUserReqBody()
        response = update_user_api(function_user.id, payload)
        assert_status_code(response.status_code, HTTPStatus.OK)
        json_response: User = response.json()
        validate_schema(json_response, ModelUser.schema())

    @allure.title('Delete User')
    def test_delete_user(self, function_user: ModelUser):
        payload = ModelUserReqBody()
        response = delete_user_api(user_id=function_user.id)
        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)

    @allure.title('Add User')
    def test_add_user(self):
        payload = ModelUserReqBody()
        response = add_user_api(payload)
        json_response: UserBodyClass = response.json()
        assert_status_code(response.status_code, HTTPStatus.CREATED)
        validate_schema(json_response, ModelUserReqBody.schema())
        # print(ModelUserBody().dict(by_alias=True))

    @allure.title('Get account')
    def test_get_account(self):
        # payload = ModelAccountBody()
        response = get_account_api(account_id=1)
        json_response: AccountClass = response.json()
        # print(json_response)
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_schema(json_response, ModelAccount.schema())

    @allure.title('Delete Account')
    def test_delete_account(self, function_account: ModelAccount):
        payload = ModelAccountReqBody()
        response = delete_account_api(account_id=function_account.id)
        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)

    @allure.title('Update account')
    def test_update_account(self, function_account: ModelAccount):
        # response = get_account_api(account_id=function_account.id)
        # print(response.json())
        payload = ModelAccount(brief=function_account.brief,
                               dateEnd=function_account.dateEnd,
                               dateStart=function_account.dateStart,
                               fund_id=function_account.fund_id,
                               id=function_account.id,
                               name="Счет ПЕРЕИМЕНОВАННЫЙ 22",
                               user_id=function_account.user_id)
        # print(payload)
        response = update_account_api(function_account.id, payload)
        json_response: AccountClass = response.json()
        # print(json_response)
        assert_status_code(response.status_code, HTTPStatus.OK)
        # json_response: User = response.json()
        validate_schema(json_response, ModelAccount.schema())

    @allure.title('Add account')
    def test_add_account(self):
        payload = ModelAccountReqBody()
        response = add_account_api(payload)
        json_response: AccountClass = response.json()
        # print(json_response)
        assert_status_code(response.status_code, HTTPStatus.CREATED)
        validate_schema(json_response, ModelAccount.schema())
