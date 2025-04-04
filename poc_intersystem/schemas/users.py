from pydantic import BaseModel, ConfigDict, EmailStr


class UserInput(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
