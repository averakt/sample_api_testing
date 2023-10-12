from typing import TypedDict
from pydantic import BaseModel, Field
from utils.fakers import random_list_of_strings, random_number, random_string
from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Links:
    next: int | None
    prev: int | None
    self: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        _next = obj.get("next")
        _prev = obj.get("prev")
        _self = str(obj.get("self"))
        return Links(_next, _prev, _self)


@dataclass
class Links2:
    avatar: str
    followed: str
    followers: str
    self: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links2':
        _avatar = str(obj.get("avatar"))
        _followed = str(obj.get("followed"))
        _followers = str(obj.get("followers"))
        _self = str(obj.get("self"))
        return Links2(_avatar, _followed, _followers, _self)


@dataclass
class Item:
    _links: Links2
    about_me: Any
    followed_count: int
    follower_count: int
    id: int
    last_seen: str
    post_count: int
    username: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        __links = Links.from_dict(obj.get("_links"))
        _about_me = obj.get("about_me")
        _followed_count = int(obj.get("followed_count"))
        _follower_count = int(obj.get("follower_count"))
        _id = int(obj.get("id"))
        _last_seen = str(obj.get("last_seen"))
        _post_count = int(obj.get("post_count"))
        _username = str(obj.get("username"))
        return Item(__links, _about_me, _followed_count, _follower_count, _id, _last_seen, _post_count, _username)


@dataclass
class Meta:
    page: int
    per_page: int
    total_items: int
    total_pages: int

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        _page = int(obj.get("page"))
        _per_page = int(obj.get("per_page"))
        _total_items = int(obj.get("total_items"))
        _total_pages = int(obj.get("total_pages"))
        return Meta(_page, _per_page, _total_items, _total_pages)


@dataclass
class Root:
    _links: Links
    _meta: Meta
    items: List[Item]

    # @staticmethod
    # def from_dict(obj: Any) -> 'Root':
    #     __links = Links2.from_dict(obj.get("_links"))
    #     __meta = Meta.from_dict(obj.get("_meta"))
    #     _items = [Item.from_dict(y) for y in obj.get("items")]
    #     return Root(__links, __meta, _items)


class DefaultUsers(BaseModel):
    links: Links = Field(alias='_links', default={'next': random_number(),
                                                  'prev': random_number(),
                                                  'self': random_string()})
    meta: Meta = Field(alias='_meta', default={"page": random_number(),
                                               "per_page": random_number(),
                                               "total_items": random_number(),
                                               "total_pages": random_number()
                                               })
    items: List[Item] = [
        {
            "_links": {
                "avatar": "https://www.gravatar.com/avatar/41bd43acfabdbfcdfa227273d9cd4c0e?d=identicon&s=128",
                "followed": "/api/v1/users/3/followed",
                "followers": "/api/v1/users/3/followers",
                "self": "/api/v1/users/"+str(random_number())
            },
            "about_me": "null",
            "followed_count": random_number(),
            "follower_count": random_number(),
            "id": 3,
            "last_seen": "2023-09-26T18:01:36.767884Z",
            "post_count": random_number(),
            "username": "user1"
        },
        {
            "_links": {
                "avatar": "https://www.gravatar.com/avatar/d90c37a3aec6510afa8f028a4996d26c?d=identicon&s=128",
                "followed": "/api/v1/users/4/followed",
                "followers": "/api/v1/users/4/followers",
                "self": "/api/v1/users/4"
            },
            "about_me": "null",
            "followed_count": 0,
            "follower_count": 0,
            "id": 4,
            "last_seen": "2023-09-26T18:47:57.139992Z",
            "post_count": 0,
            "username": "user2"
        }
    ]
