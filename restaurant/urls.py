from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('sayHello', views.sayHello, name='sayHello'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth-token/', obtain_auth_token)
]
