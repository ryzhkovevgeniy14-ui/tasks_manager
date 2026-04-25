# REST API для управления задачами, реализованное на FastAPI.

## Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск сервера
```bash
uvicorn app.main:app --reload
```

## Эндпоинты
### Создать задачу
```http
POST /tasks
```
### Получить все задачи
```http
GET /tasks
```
### Получить задачу по id
```http
GET /tasks/{task_id}
```

## Технологии
- **Python**
- **FastAPI**
- **Pydantic**
