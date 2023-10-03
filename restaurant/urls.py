from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    # path('sayHello', views.sayHello, name='sayHello'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
