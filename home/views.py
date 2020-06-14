from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from .models import Message

def homePage(request):
    content={
        'items':Item.objects.all().first(),
        'slides':Slide.objects.all(),
        'sponsors':Sponsor.objects.all()
    }
    return render(request, 'home/home.html',content)

@api_view(['GET'])
def saveMsg(request):
    # name = request.GET['name']
    # email = request.GET['email']
    # mobile = request.GET['mobile']
    # subject = request.GET['subject']
    # msg = request.GET['msg']
    # messa = Message(name=name,email=email,mobile=mobile,subject=subject,message=msg)
    # messa.save()
    msg = Message.objects.all()
    serializer = MessageSerializer(msg, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def svMsg(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)