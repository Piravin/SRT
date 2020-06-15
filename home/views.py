from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
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
    msg = Message.objects.all()
    serializer = MessageSerializer(msg, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def svMsg(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def showSlide(request):
    slide = Slide.objects.all()
    serializer = SlideSerializer(slide, many=True)
    return Response(serializer.data)

def carsPage(request):
    content={
        'cars':Car.objects.all().first(),
        'items':Item.objects.only('logo').first()}
    return render(request,'home/cars.html',content)