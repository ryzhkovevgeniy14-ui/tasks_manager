from app.schemas.task import TaskCreate, Task


class TaskService:
    """
    Класс для управления задачами.
    Хранит список задач и их уникальные ID в памяти.
    """
    def __init__(self):
        self.tasks: list[Task] = []
        self.current_id: int = 1

    # Метод для создания новой задачи
    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(id=self.current_id, **task_data.model_dump())
        self.tasks.append(task)
        self.current_id += 1
        return task

    # Метод для получения всех задач
    def get_tasks(self) -> list[Task]:
        return self.tasks

    # Метод для получения задачи по ID
    def get_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError("Task not found")


task_service = TaskService()
