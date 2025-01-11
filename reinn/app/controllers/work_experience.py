from fastapi import APIRouter,Depends
from..database import get_db
from ..models.work_experience import WorkExperience
from ..services.work_experience import create_work_experience
from..views.work_experience import *
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()
@router.post("/work-experience", response_model=WorkExperienceResponse,tags=["work-experience"])
async def create_work_experience_endpoint(work_experience: WorkExperienceRequest, session: AsyncSession = Depends(get_db)):
    await create_work_experience(session, work_experience)






