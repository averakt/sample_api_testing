import pytest

from base.api.questions_api import (create_user, delete_user_api, create_account,
                                    delete_account_api)
from models.users import User
from models.accounts import AccountClass


@pytest.fixture(scope='function')
def function_user() -> User:
    user = create_user()

    yield user

    delete_user_api(user.id)


@pytest.fixture(scope='function')
def function_account() -> AccountClass:
    account = create_account()

    yield account

    delete_account_api(account.id)
