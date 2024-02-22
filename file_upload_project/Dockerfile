FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y redis-server

WORKDIR /code

ADD . /code/
ADD .env.docker /code/.env

RUN pip install -r requirements.txt

CMD ["bash", "-c", "service redis-server start && gunicorn --bind 0.0.0.0:8000 file_upload_project.wsgi:application && celery -A file_upload_project worker --loglevel=INFO"]
