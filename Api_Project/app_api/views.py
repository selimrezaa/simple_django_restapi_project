from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .serializer import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

def index(request):
    list = Student.objects.all()
    context = {
        'list': list,
    }
    return render(request, 'index.html', context)


@api_view(['GET', 'POST'])
def student(request):
    if (request.method == "GET"):
        list = Student.objects.all()
        serializer = StudentSerializer(list, many=True)
        return Response(serializer.data)

    if (request.method == "POST"):
        data=request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'created'}
            return Response(res)
        return Response({'msg': serializer.errors})



@api_view(['GET', 'PUT', 'DELETE'])
def single_student(request, pk):
    try:
        list = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(list)
        return Response(serializer.data)

    elif request.method=='PUT':
        try:
            serializer = StudentSerializer(list, data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Student.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUIEST)

    elif request.method == "DELETE":
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#whatsapp msg

import pywhatkit

def whatsapp_msg(request,pk):
    obj = Student.objects.get(pk=pk)
    context = {
        'obj': obj,
    }
    msg = pywhatkit.sendwhatmsg('+88+obj','ok', 14, 7)
    return HttpResponseRedirect(reverse('index'))



    # return render(request, 'index.html', context)


# def whtatsapp():
#     obj = Student.objects.get(pk=1).filter('phone'='phone')
#
#     msg = pywhatkit.sendwhatmsg('obj', 'ok', 13,20)
#     return msg
