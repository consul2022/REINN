from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Resume(Base):
    __tablename__ = "resume" #название таблицы в БД
    id = Column(Integer, primary_key=True) #nullable(может не заполнять), unique-уникальность(другого не должно быть пользователя)
    position = Column(String, nullable=True, unique=True)
    stack = Column(String, nullable=True, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=False)
