from django.shortcuts import render
from .models import *

def just(request):
    content={'tab':Course.objects.all().first()}
    return render(request,'courses/just.html',content)

