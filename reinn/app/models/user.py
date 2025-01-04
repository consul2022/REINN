from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()  # создали родительский класс для модели


class User(Base):
    __tablename__="user" #название таблицы в БД
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False, unique=False) #nullable(может не заполнять), unique-уникальность(другого не должно быть пользователя)
    list_name = Column(String, nullable=True, unique=False)
    phone = Column(Integer, nullable=True, unique=True)
    email = Column(String, nullable=False, unique=True)
    telegramm = Column(String, nullable=True, unique=True)
    leetcode = Column(String, nullable=True, unique=True)
    github = Column(String, nullable=True, unique=True)
    photo = Column(String, nullable=True, unique=True)


