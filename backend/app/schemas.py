from typing import Optional
from pydantic import BaseModel

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для представления пользователя
class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True

# Схема для аутентификации пользователя
class UserLogin(BaseModel):
    username: str
    password: str

# Схема для представления токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Схема для данных токена
class TokenData(BaseModel):
    username: Optional[str] = None
