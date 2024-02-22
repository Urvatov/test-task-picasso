from django.contrib import admin
from django.urls import path

from app.views import upload

urlpatterns = [
    path('admin/', admin.site.urls),

    path('upload/', upload, name="upload-file")
]
