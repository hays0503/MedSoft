from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from . import models
from .database import get_db, engine
from .auth import create_access_token, get_current_user, get_password_hash, authenticate_user,ACCESS_TOKEN_EXPIRE_MINUTES  # Убедитесь, что эти функции импортированы из auth.py
from .schemas import PasswordRecoveryRequest, Message
from .schemas import UserCreate,UserLoginPhone, Token, User as SchemaUser  # Изменено для ясности и избежания конфликтов имен
from .recovery_password import generate_password_reset_token,send_password_reset_confirmation_email, send_password_reset_email
from .generate_password import generate_ascii_password

# Создание таблиц в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/users/registration", response_model=SchemaUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database.

    Args:
        user (UserCreate): The user data to be created.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        SchemaUser: The created user data.

    Raises:
        HTTPException: If the username is already registered.
    """
    db_user = db.query(models.User).filter(models.User.phone == user.phone.number).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Phone already registered")
    hashed_password = get_password_hash(user.password)
    db_user = models.User(phone=user.phone.number,username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/users/authenticate/user-password", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Endpoint to authenticate a user and generate an access token.

    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the access token and token type.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/authenticate/phone-password", response_model=Token)
def login_for_access_token(form_data: UserLoginPhone = Depends(), db: Session = Depends(get_db)):
    """
    Endpoint to authenticate a user and generate an access token using phone and password.

    Args:
        form_data (UserLoginPhone): The form data containing the phone and password.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the access token and token type.
    """
    user = authenticate_user(db, form_data.phone.phone, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Эндпоинт для запроса на восстановление пароля
@app.post("/password-recovery/", response_model=Message)
async def recover_password(request_data: PasswordRecoveryRequest, request: Request, db: Session = Depends(get_db)):
   
    email = request_data.email
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found")
    
    token = generate_password_reset_token(email)
    try:
        send_password_reset_email(email, token,request.url)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to send recovery email")

    user.password_reset_token = token

    # обновление токена в базе данных
    db.commit()
      
    return {"message": "Password recovery email sent"}

@app.get("/password-recovery/token/{token_date}/", response_model=Message)
async def reset_password(token_date: str, db: Session = Depends(get_db)):
    # Проверка наличия токена в базе данных
    user = db.query(models.User).filter(models.User.password_reset_token == token_date).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token not found")

    # Обновление пароля пользователя
    
    new_password = generate_ascii_password(12)
    
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password

    # Отправка подтверждения на почту
    try:
        send_password_reset_confirmation_email(user.email, new_password)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to send reset confirmation email")
    
    # Удаление токена сброса пароля
    user.password_reset_token = None
    
    db.commit()
    
    return {"message": "Password reset successful"}


@app.get("/users/me/", response_model=SchemaUser)
def read_users_me(current_user: SchemaUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Retrieve the details of the currently authenticated user.

    Parameters:
    - current_user: The currently authenticated user.
    - db: The database session.

    Returns:
    - The details of the currently authenticated user.
    """
    # Ваша логика здесь...
    return current_user
