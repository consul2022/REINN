from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..database import Base



class Resume(Base):
    __tablename__ = "resume"  # название таблицы в БД
    id = Column(Integer,
                primary_key=True, index=True)  # nullable(может не заполнять), unique-уникальность(другого не должно быть пользователя)
    position = Column(String, nullable=True, unique=True)
    stack = Column(String, nullable=True, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, unique=False)

    """связь модели с user"""
    user = relationship("User", back_populates="resumes")
    educations = relationship("Education", back_populates="resume")
    work_experiences = relationship("WorkExperience", back_populates="resume")
    my_projects = relationship("MyProject", back_populates="resume")
    start_ups = relationship("StartUp", back_populates="resume")
