import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_upload_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#python manage.py runserver
#python manage.py makemigrations
#python manage.py migrate
    
def runserver():
    if "runserver" not in sys.argv:
        sys.argv.append("runserver")

if __name__ == '__main__':
    runserver()
    main()
