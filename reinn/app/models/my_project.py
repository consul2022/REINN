from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class MyProject(Base):
    __tablename__ = "my_project"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=False)
    description = Column(String, nullable=False, unique=False)
    link_site = Column(String, nullable=True, unique=False)
    link_git = Column(String, nullable=True, unique=False)
    responsibilities = Column(String, nullable=True, unique=False)
    achievements = Column(String, nullable=True, unique=False)
    stack = Column(String, nullable=True, unique=False)
    resume_id = Column(Integer, ForeignKey("resume.id"), nullable=False, unique=False)

    resume = relationship("Resume", back_populates="my_projects")
