from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.filters import SearchFilter

from .serializers import *


# TODO: User
class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserAPIView(APIView):
    def get_user(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)


# TODO: ProductCategory
class ProductCategoryListAPIView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductCategoryAPIView(APIView):
    def get_category(self, pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
            return category
        except ProductCategory.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def post(self, request):
        serializer = ProductCategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        category = self.get_category(pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_category(pk)
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_category(pk)
        category.delete()
        return Response(status=status.HTTP_200_OK)


# TODO: Product
class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductCategorySerializer(products, many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    def get_product(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product(pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)


class ProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# TODO: Order
class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    filter_backends = [SearchFilter]
    search_fields = ['order_status', 'email']

    queryset = Order.objects.all()


class OrderCreateAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        queryset = Order.objects.filter(email=email).count()
        print(queryset)

        # serializer = OrderCreateSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Update order status

class OrderCancelAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        print(id)
        # if id:
        #     queryset = Order.objects.filter()
        # else:
        #     queryset = User.objects.all()
        #
        # return queryset
