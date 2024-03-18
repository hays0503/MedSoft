from datetime import timedelta
from .auth import create_access_token,SECRET_KEY,ALGORITHM
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from .email_sender import EmailSender

# Функция для генерации токена сброса пароля
def generate_password_reset_token(email: str) -> str:
    token_data = {"email": email}
    return create_access_token(data=token_data, expires_delta=timedelta(hours=24))

# Функция для отправки электронного письма с ссылкой на сброс пароля
def send_password_reset_email(email: str, token: str, url: str):
    # Ваш код для отправки электронного письма с ссылкой на сброс пароля
    sender_email = 'MedSoft@mail.kz'
    sender_password = 'i@xngj6GXs8ANPk'

    email_sender = EmailSender(sender_email, sender_password)
    email_sender.send_email(email, "Востановление пароля от кабинета", f"Для восстановления пароля перейдите по ссылке {url}token/{token}")

# Функция для отправки электронного письма с ссылкой на сброс пароля
def send_password_reset_confirmation_email(email: str, password: str):
    # Ваш код для отправки электронного письма с ссылкой на сброс пароля
    sender_email = 'MedSoft@mail.kz'
    sender_password = 'i@xngj6GXs8ANPk'

    email_sender = EmailSender(sender_email, sender_password)
    email_sender.send_email(email, "Новый пароль:", password)


# Функция для сброса пароля
async def reset_password(token: str, new_password: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
        # Ваш код для сброса пароля
        # Например, можно использовать email для поиска пользователя в базе данных
        # И установить новый пароль для найденного пользователя
    except JWTError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
