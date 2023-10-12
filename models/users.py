from pydantic import BaseModel, Field
from utils.fakers import random_number, random_string
from typing import Any
from dataclasses import dataclass


@dataclass
class Links:
    avatar: str
    followed: str
    followers: str
    self: str


@dataclass
class UserBodyClass:
    username: str
    email: str
    password: str
    last_name: str
    first_name: str
    patronymic: str

    @staticmethod
    def from_dict(obj: Any) -> 'UserBodyClass':
        _username = str(obj.get("username"))
        _email = str(obj.get("email"))
        _password = str(obj.get("password"))
        _last_name = str(obj.get("last_name"))
        _first_name = str(obj.get("first_name"))
        _patronymic = str(obj.get("patronymic"))
        return UserBodyClass(_username, _email, _password, _last_name, _first_name, _patronymic)


class ModelUserReqBody(BaseModel):
    username: str = "user_"+random_string()
    email: str = "email"+"@"+random_string()+".com"
    password: str = Field(default="pswdfortest")
    last_name: str = "last_name_"+random_string()
    first_name: str = "first_name_"+random_string()
    patronymic: str | None = "patronymic_"+random_string()


@dataclass
class User:
    _links: Links
    about_me: str
    followed_count: int
    follower_count: int
    id: int
    last_seen: str
    post_count: int
    username: str


class ModelUser(BaseModel):
    links: Links = Field(alias='_links', default={
                "avatar": "https://www.gravatar.com/avatar/41bd43acfabdbfcdfa227273d9cd4c0e?d=identicon&s=128",
                "followed": "/api/v1/users/3/followed",
                "followers": "/api/v1/users/3/followers",
                "self": "/api/v1/users/"+str(random_number())
                })
    about_me: Any = ""
    followed_count: int = random_number()
    follower_count: int = random_number()
    id: int = random_number()
    last_seen: str = "2023-09-27T17:32:47.289648Z"
    post_count: int = random_number()
    username: str = "user_"+str(random_number())
