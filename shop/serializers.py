from rest_framework.serializers import ModelSerializer

from .models import *


# User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'surname',
            'name',
            'patronymic',
            'full_name',
            'email',
            'creation_date',
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'surname',
            'name',
            'patronymic',
            'email',
        ]


# ProductCategory
class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'id',
            'title',
            'url',
        ]


class ProductCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'title',
            'url',
        ]


# Product
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'manufacturer',
            'model',
            'production_date',
            'color',
            'cost',
            'full_title',
        ]


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'manufacturer',
            'model',
            'production_date',
            'color',
            'cost',
        ]


# Order
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'email',
            'product',
            'amount',
            'order_time',
            'comment',
            'order_status',
            'total_cost',
        ]


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'email',
            'product',
            'amount',
            'comment',
        ]