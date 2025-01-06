from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..database import Base
  # создали родительский класс для модели


class User(Base):
    __tablename__ = "user"  # название таблицы в БД
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False,
                        unique=False)  # nullable(может не заполнять), unique-уникальность(другого не должно быть пользователя)
    list_name = Column(String, nullable=True, unique=False)
    phone = Column(Integer, nullable=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    telegramm = Column(String, nullable=True, unique=True)
    leetcode = Column(String, nullable=True, unique=True)
    github = Column(String, nullable=True, unique=True)
    photo = Column(String, nullable=True, unique=True)

    """связь модели с user"""
    resumes = relationship("Resume", back_populates="user")
    post_users = relationship("PostUser", back_populates="user")
    post_comments = relationship("PostComment", back_populates="user")

