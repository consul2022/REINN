from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..database import Base



class PostUser(Base):
    __tablename__ = "post_user"  # название таблицы в БД
    id = Column(Integer,
                primary_key=True,
                index=True)  # nullable(может не заполнять), unique-уникальность(другого не должно быть пользователя)
    post_name = Column(String, nullable=True, unique=False)
    time_post = Column(DateTime, nullable=True, unique=False)
    description = Column(String, nullable=True, unique=False)
    like = Column(Integer, nullable=True, unique=False)
    views = Column(Integer, nullable=True, unique=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=False)

    user = relationship("User", back_populates="post_users")
    post_documents = relationship("PostDocument", back_populates="post_user")
    post_comments = relationship("PostComment", back_populates="post_user")
