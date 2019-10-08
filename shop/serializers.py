from rest_framework.serializers import ModelSerializer

from .models import *


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


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        exclude = ['id']


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
            'currency',
            'full_title',
        ]


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']


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


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class BillCreateSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = [
            'email',
            'money',
            'currency',
        ]
