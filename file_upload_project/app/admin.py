from django.contrib import admin

from app.models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'processed')