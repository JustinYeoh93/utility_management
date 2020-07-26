from pydantic import BaseModel, EmailStr, validator
from cuid import cuid
import base64
import hashlib
import bcrypt


class User(BaseModel):
    id: str = ""
    user_name: str
    password: str
    email: EmailStr

    @validator("id", always=True)
    def default_id(cls, v):
        if v:
            return v
        return str(cuid())

    @validator("username")
    def trim_name(cls, v):
        return v.strip()

    @validator("password")
    def hash_password(cls, v):
        crypto_v = base64.b64encode(hashlib.sha256(str.encode(v)).digest())
        hashpw = bcrypt.hashpw(crypto_v, bcrypt.gensalt())
        return hashpw


class Room(BaseModel):
    id = str = ""
    room_name = str
    admin_id = str

    @validator("id", always=True)
    def default_id(cls, v):
        if v:
            return v
        return str(cuid())

    @validator("room_name")
    def trim_name(cls, v):
        return v.strip()


class Item(BaseModel):
    item_name = str
    quantity = float
    room_id = str

    @validator("item_name", always=True)
    def trim_name(cls, v):
        return v.strip()

    @validator("quantity")
    def no_negatives(cls, v):
        if v < 0:
            return 0
        return v


class Member(BaseModel):
    user_id: str
    room_id: str
