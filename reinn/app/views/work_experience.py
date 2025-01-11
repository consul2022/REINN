from pydantic import BaseModel
import datetime

class WorkExperienceBase(BaseModel):
    start_date: str
    end_date: str
    company_name: str
    position: str
    company_description: str
    link: str
    responsibilities: str
    achievements: str
    resume_id: int
    class Config:
        orm_mode = True

class WorkExperienceResponse(WorkExperienceBase):
    id: str



class WorkExperienceRequest(WorkExperienceBase):
    pass










