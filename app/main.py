from fastapi import FastAPI
from app.routers.tasks import router as tasks_router


# Экземпляр приложения FastAPI
app = FastAPI()

# Подключаем маршрутизатор задач к приложению
app.include_router(tasks_router)