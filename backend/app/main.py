from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from . import models
from .database import get_db, engine
from .auth import create_access_token, get_current_user, get_password_hash, authenticate_user,ACCESS_TOKEN_EXPIRE_MINUTES  # Убедитесь, что эти функции импортированы из auth.py
from .schemas import UserCreate, Token, User as SchemaUser  # Изменено для ясности и избежания конфликтов имен

# Создание таблиц в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/users/", response_model=SchemaUser)
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
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/token", response_model=Token)
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
