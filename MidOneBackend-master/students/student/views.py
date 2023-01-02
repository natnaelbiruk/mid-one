from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import studentclass
from .serializers import stuSerializers
@api_view(['GET'])
def studentList(request):
     student=studentclass.objects.all().order_by('-id')
     serialdata=stuSerializers(student,many=True)
     return Response(serialdata.data)
@api_view(['POST'])
def AddStu(request):
      serializer=stuSerializers(data=request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)
@api_view(['POST'])
def update(request,pk):
     stuupdate=studentclass.objects.get(id=pk)
     serial=stuSerializers(instance=stuupdate,data=request.data)
     if serial.is_valid():
            serial.save()
     return Response(serial.data)
@api_view(['DELETE'])
def deleteStu(request,pk):
     studelete=studentclass.objects.get(id=pk)
     studelete.delete()
     return Response('deleted succesfully')