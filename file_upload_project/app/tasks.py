from file_upload_project.celery import capp
from celery import shared_task
from time import sleep

from app.models import File


@capp.task
def process_file(file_id):
    print("ожидание...")
    sleep(5)
    file_instance = File.objects.get(pk=file_id)
    file_instance.processed = True
    file_instance.save() 
    print("готово")
    


# celery -A file_upload_project worker -l info
# celery -A file_upload_project --loglevel=INFO --pool=solo 
# celery -A celery:capp --loglevel=INFO --pool=solo 
    
#celery -A file_upload_project worker -l info -P solo