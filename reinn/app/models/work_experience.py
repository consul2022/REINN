import enum

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PositionName(enum.Enum):
    INTERN = "Стажер"
    JUNIOR = "Младший разработчик"
    MIDDLE = "Разработчик"
    SENIOR = "Старший разработчик"
    LEAD = "Ведущий разработчик"
    PRINCIPAL = "Главный разработчик"
    STAFF = "Штатный разработчик"
    ARCHITECT = "Архитектор программного обеспечения"
    CTO = "Технический директор"


class WorkExperience(Base):
    __tablename__ = "work_experience"
    id = Column(Integer, primary_key=True, index=True)
    start_data = Column(Date, nullable=True, unique=False)
    end_date = Column(Date, nullable=True, unique=False)
    company_name = Column(String, nullable=False, unique=False)
    position = Column(Enum(PositionName), nullable=False, unique=False)
    company_description = Column(String, nullable=False, unique=False)
    link = Column(String, nullable=True, unique=False)
    responsibilities = Column(String, nullable=False, unique=False)
    achievements = Column(String, nullable=False, unique=False)
    resume_id = Column(Integer, ForeignKey("resume.id"), nullable=False, unique=False)

    resume = relationship("Resume", back_populates="work_experiences")
