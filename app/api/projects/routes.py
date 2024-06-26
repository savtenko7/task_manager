from fastapi import APIRouter, Depends

from app.api.dependencie import CurrentUser
from app.schemas.projects import CreateProject
from app.services.project_service import ProjectService

router = APIRouter(

    tags=['project'],

    prefix='/projects',

    )


@router.post('/create')
async def create_project(user: CurrentUser,
                         project_data: CreateProject,
                         project_service: ProjectService = Depends(),
                         ):
    return await project_service.create_project(
        user.id,
        project_data
    )


@router.get('/list')
async def get_projects(user: CurrentUser,
                        project_service: ProjectService = Depends(),
                        ):

    return await project_service.get_project_with_tasks({"user_id":user.id})
