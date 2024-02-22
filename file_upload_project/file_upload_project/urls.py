from django.contrib import admin
from django.urls import path

from app.views import upload_file

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload-file/', upload_file, name="upload-file")
]
