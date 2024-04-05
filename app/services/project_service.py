from fastapi import Depends

from app.repository.project_repository import ProjectRepository
from app.schemas.projects import CreateProject, ProjectInDB


class ProjectService:
    def __init__(
            self, project_repo: ProjectRepository = Depends(),
    ):
        self.project_repo: ProjectRepository = project_repo

    async def create_project(
            self,
            user_id: int,
            project_data: CreateProject,
    ):

        project_data = ProjectInDB(
            **project_data.model_dump(),
            user_id=user_id,
        )

        return await self.project_repo.create(project_data.model_dump())
