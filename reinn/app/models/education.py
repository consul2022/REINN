import enum
from ..database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class EducationLevel(enum.Enum):
    POSTGRADUATE_STUDIES = "Аспирантура"
    MASTERS_DEGREE = "Магистратура"
    SPECIALTY_DEGREE = "Специалитет"
    BACHELORS_DEGREE = "Баклавриат"
    SECONDARY_VOCATIONAL = "Среднее проффесиональное образование"
    SECONDARY_GENERAL = "Среднее общее образование"


class Education(Base):
    __tablename__ = "education"
    id = Column(Integer,primary_key=True, index=True)
    start_data = Column(Date, nullable=True, unique=False)
    end_date = Column(Date, nullable=True, unique=False)
    level = Column(Enum(EducationLevel), nullable=False, unique=False)
    name_institution = Column(String, nullable=False, unique=False)
    faculty = Column(String, nullable=False, unique=False)
    direction = Column(String, nullable=False, unique=False)
    resume_id = Column(Integer, ForeignKey("resume.id"), nullable=False, unique=False)

    resume = relationship("Resume", back_populates="educations")
