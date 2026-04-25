from fastapi import APIRouter, HTTPException, status

from app.schemas.task import Task, TaskCreate
from app.services.task_service import task_service


# Экземпляр маршрутизатора для задач
router = APIRouter(prefix="/tasks", tags=["tasks"])


# Эндпоинт для создания новой задачи
@router.post("/", response_model=Task)
async def create_task(task: TaskCreate):
    return task_service.create_task(task)


# Эндпоинт для получения списка всех задач
@router.get("", response_model=list[Task])
async def get_tasks():
    return task_service.get_tasks()


# Эндпоинт для получения задачи по её ID
@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    try:
        return task_service.get_task(task_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")