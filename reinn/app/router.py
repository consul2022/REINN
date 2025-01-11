from fastapi import APIRouter

from reinn.app.controllers import work_experience

root_api_router = APIRouter(prefix="/api")

root_api_router.include_router(work_experience.router, tags=["work_experience"])
