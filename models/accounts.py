from pydantic import BaseModel
from utils.fakers import random_number, random_acc_number
from dataclasses import dataclass


@dataclass
class AccountReqBodyClass:
    brief: str
    fund_id: int
    name: str
    user_id: int


class ModelAccountReqBody(BaseModel):
    brief: str = "423028106000000"+str(random_acc_number())
    fund_id: int = 2
    name: str = "Счет до востребования"
    user_id: int = 1


@dataclass
class AccountClass:
    brief: str
    dateEnd: str
    dateStart: str
    fund_id: int
    id: int
    name: str
    user_id: int


class ModelAccount(BaseModel):
    brief: str = "423018106000000"+str(random_acc_number())
    dateEnd: str = "1900-01-01T00:00:00Z"
    dateStart: str = "2023-09-26T19:52:09.166208Z"
    fund_id: int = 2
    id: int = random_number(start=1000, end=2000)
    name: str = "Счет до востребования"
    user_id: int = 1
