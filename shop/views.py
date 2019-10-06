from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter

from .serializers import *


# User
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ProductCategory
class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


@csrf_exempt
def category_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductCategoryCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class ProductCategoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


# Product
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class ProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Order
class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    filter_backends = [SearchFilter]
    search_fields = ['order_status']

    queryset = Order.objects.all()

    # def get_queryset(self):
    #     is_with_task = self.request.GET.get('order_status')
    #     if is_with_task:
    #         queryset = Order.objects.exclude(assigned_tasks__assigned__isnull=True)
    #     else:
    #         queryset = Order.objects.all()
    #
    #     return queryset


@csrf_exempt
def order_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)


class OrderAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
