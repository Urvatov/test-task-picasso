from django.shortcuts import render
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
        file = serializer.save()
        process_file.delay(file.instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

