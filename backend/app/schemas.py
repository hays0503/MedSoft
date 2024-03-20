from typing import Optional
from typing_extensions import Annotated
from fastapi import Form
from pydantic import BaseModel, Field, StringConstraints, ValidationError, validator 

class Message(BaseModel):
    message: str

# Модель данных для JSON запроса на восстановление пароля
class PasswordRecoveryRequest(BaseModel):
    email: str

class Phone(BaseModel):
    number: Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, pattern=r'^\+\d{11}$')]

    @validator('number')
    def validate_phone(cls, v):
        if not v.startswith('+'):
            raise ValueError('Номер телефона должен начинаться с +')
        return v.replace(' ', '')

    class Config:
        from_attributes = True

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    # Номер телефона пользователя (формат: +71234567890)
    phone: Phone

# Схема для представления пользователя
class User(BaseModel):
    id: int
    username: str
    email: str
    phone: str
    is_active: bool

    class Config:
        from_attributes = True

# Схема для аутентификации пользователя
class UserLogin(BaseModel):
    username: str = Field(..., alias="username")
    password: str = Field(..., alias="password")

    # @validator('username', 'password')
    # def parse_form_data(cls, v):
    #     return v[0] if isinstance(v, list) else v



# Схема для аутентификации пользователя по телефону
class UserLoginPhone(BaseModel):
    phone: Phone
    password: str

# Схема для представления токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Схема для данных токена
class TokenData(BaseModel):
    username: Optional[str] = None
