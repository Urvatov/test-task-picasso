# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем Redis
RUN apt-get update && \
    apt-get install -y redis-server

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем файлы вашего приложения и устанавливаем зависимости
ADD . /code/
ADD .env.docker /code/.env

RUN pip install -r requirements.txt

# Команда для запуска Redis и Django приложения
CMD ["bash", "-c", "service redis-server start && gunicorn --bind 0.0.0.0:8000 file_upload_project.wsgi:application"]
