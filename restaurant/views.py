from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import Menu
from .serializers import MenuSerializer


def index(request):
    return render(request, 'index.html', {})

# Create your views here.


def sayHello(request):
    return HttpResponse('Hello World')


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
