from typing import TypedDict


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
