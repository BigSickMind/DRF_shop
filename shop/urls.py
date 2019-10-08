from django.urls import path

from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),

    path('category/', ProductCategoryListAPIView.as_view()),
    path('category/<int:pk>/', ProductCategoryAPIView.as_view()),

    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView.as_view()),

    path('order/create/', OrderCreateAPIView.as_view()),
    path('order/', OrderListAPIView.as_view()),
    path('order/<int:pk>/', OrderAPIView.as_view()),

    path('bill/', BillListAPIView.as_view()),
    path('bill/<int:pk>/<int:money>/', BillAPIView.as_view()),
]
