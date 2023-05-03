from django.shortcuts import render
from . models import jadwal
from . serializers import jadwalserializer

#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#create your view here
@api_view(['GET'])
def readjadwal(request):
    jadwal_imsyak = jadwal.objects.all()
    serializer = jadwalserializer(jadwal_imsyak, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createjadwal(request):
    serializer = jadwalserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
