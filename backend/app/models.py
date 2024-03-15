from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.
        is_active (bool): Indicates whether the user is active or not.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Если у вас есть отношения с другими таблицами, вы можете использовать relationship для их определения
    # items = relationship("Item", back_populates="owner")
