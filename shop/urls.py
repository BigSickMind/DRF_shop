from django.urls import path

from .views import *

urlpatterns = [
    # Users
    path('users/create/', user_create),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('users/<int:pk>/edit/', UserAPIView.as_view()),
    path('users/<int:pk>/delete/', UserAPIView.as_view()),

    # ProductCategories
    path('category/create/', category_create),
    path('category/', ProductCategoryListAPIView.as_view()),
    path('category/<int:pk>/', ProductCategoryAPIView.as_view()),
    path('category/<int:pk>/edit/', ProductCategoryAPIView.as_view()),
    path('category/<int:pk>/delete/', ProductCategoryAPIView.as_view()),

    # Product
    path('product/create/', product_create),
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView.as_view()),
    path('product/<int:pk>/edit/', ProductAPIView.as_view()),
    path('product/<int:pk>/delete/', ProductAPIView.as_view()),

    # Order
    path('order/create/', order_create),
    path('order/', OrderListAPIView.as_view()),
    path('order/<int:pk>/cancel/', OrderAPIView.as_view()),
]
