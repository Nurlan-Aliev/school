from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    name: str
    surname: str
    age: int
    username: str
    email_address: EmailStr


class CreateUser(UserBase):
    password: bytes


class ReadUser(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UpdateUser(UserBase):
    name: str | None = None
    surname: str | None = None
    age: int | None = None
    username: str | None = None
    email_address: EmailStr | None = None
