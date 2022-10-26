import types
from typing import Final, TypeAlias, TypedDict

Email: TypeAlias = str

USERS_API_URL: Final = 'https://jsonplaceholder.typicode.com/users'


# Response types
class User(TypedDict):
    id: int
    email: str


class Post(TypedDict):
    id: int
    title: str
    body: str


class Album(TypedDict):
    id: int
    title: str


class Todo(TypedDict):
    id: int
    title: str
    completed: bool


class UserAttrs(TypedDict):
    posts: list[Post]
    albums: list[Album]
    todos: list[Todo]


USER_ATTR_NAMES: Final = UserAttrs.__annotations__.keys()

BINDINGS: Final = types.MappingProxyType({
    'posts': Post,
    'albums': Album,
    'todos': Todo,
})
