from sqlalchemy.ext.asyncio import AsyncSession

from ..models.work_experience import WorkExperience
from ..views.work_experience import WorkExperienceRequest


async def create_work_experience(session: AsyncSession, work_experience: WorkExperienceRequest):
    return await WorkExperience.add_work_experience(session, work_experience)