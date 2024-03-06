from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])#The api_view decorator specifies that the view only accepts HTTP GET and POST requests. 
@permission_classes([IsAuthenticated])#The permission_classes decorator specifies that only authenticated users (IsAuthenticated) have permission to access this view.
def schoolJsonData(request):
    SOD=School.objects.all()
    JOD=SchoolModelSerializer(SOD,many=True)
    jsondata=JOD.data
    return Response(jsondata)