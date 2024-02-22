from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.serializers import FileSerializer
from app.tasks import process_file

from app.models import File

@api_view(['POST'])
def upload(request):
    serializer = FileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        process_file.delay(serializer.instance.id) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)


def index(request):
    return HttpResponse('<h1>Приложение работает.</h1>')