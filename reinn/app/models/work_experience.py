import enum

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Enum
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from ..database import Base
from ..views.work_experience import WorkExperienceRequest


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
    start_date = Column(Date, nullable=True, unique=False)
    end_date = Column(Date, nullable=True, unique=False)
    company_name = Column(String, nullable=False, unique=False)
    position = Column(Enum(PositionName), nullable=False, unique=False)
    company_description = Column(String, nullable=False, unique=False)
    link = Column(String, nullable=True, unique=False)
    responsibilities = Column(String, nullable=False, unique=False)
    achievements = Column(String, nullable=False, unique=False)
    resume_id = Column(Integer, ForeignKey("resume.id"), nullable=False, unique=False)

    resume = relationship("Resume", back_populates="work_experiences")

    @staticmethod
    async def add_work_experience(session: AsyncSession, work_experience: WorkExperienceRequest):
        work_experience = WorkExperience(
            start_date=work_experience.start_date,
            end_date=work_experience.end_date,
            company_name=work_experience.company_name,
            link=work_experience.link,
            responsibilities=work_experience.responsibilities,
            achievements=work_experience.achievements,
            resume_id=work_experience.resume_id
        )
        session.add(work_experience)
        await session.commit()
        await session.refresh(work_experience)
        return work_experience
