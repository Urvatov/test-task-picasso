from django.contrib import admin
from django.urls import path

from app.views import upload, files, index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload/', upload, name="upload-file"),

    path('files/', files, name='file-list'),

    path('', index, name="index")
]
