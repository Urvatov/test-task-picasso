import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload_project.settings')

capp = Celery('file_upload_project')
capp.config_from_object('django.conf:settings', namespace='CELERY')
capp.autodiscover_tasks()

