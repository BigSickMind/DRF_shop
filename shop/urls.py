from django.urls import path

from .views import *

urlpatterns = [
    path('users/create/', UserAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('users/<int:pk>/edit/', UserAPIView.as_view()),
    path('users/<int:pk>/delete/', UserAPIView.as_view()),

    path('category/create/', ProductCategoryAPIView.as_view()),
    path('category/', ProductCategoryListAPIView.as_view()),
    path('category/<int:pk>/', ProductCategoryAPIView.as_view()),
    path('category/<int:pk>/edit/', ProductCategoryAPIView.as_view()),
    path('category/<int:pk>/delete/', ProductCategoryAPIView.as_view()),

    path('product/create/', ProductAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView.as_view()),
    path('product/<int:pk>/edit/', ProductAPIView.as_view()),
    path('product/<int:pk>/delete/', ProductAPIView.as_view()),

    path('order/create/', OrderCreateAPIView.as_view()),
    path('order/', OrderListAPIView.as_view()),
    path('order/<int:pk>/cancel/', OrderCancelAPIView.as_view()),
]
