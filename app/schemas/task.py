from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated


class Status(str, Enum):
    """
    Перечисление статусов задачи.
    """
    new = "new"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    """
    Модель для создания задачи.
    Используется в POST-запросах.
    """
    title: Annotated[
        str,
        Field(
            description="Название задачи"
        )
    ]
    description: Annotated[
        str | None,
        Field(
            default=None,
            description="Описание задачи")
    ]
    status: Annotated[
        Status,
        Field(
            description="Статус задачи"
        )
    ]


class Task(TaskCreate):
    """
    Модель для ответа с данными задачи.
    Используется в GET-запросах.
    """
    id: Annotated[
        int,
        Field(
            description="ID задачи"
        )
    ]