from django.http import Http404

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.filters import SearchFilter

from .serializers import *

from datetime import datetime


class UserListAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def get_user(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = self.get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryListAPIView(APIView):
    def post(self, request):
        serializer = ProductCategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryAPIView(APIView):
    def get_category(self, pk):
        try:
            category = ProductCategory.objects.get(pk=pk)
            return category
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_category(pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.get_category(pk)
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        category = self.get_category(pk)
        serializer = ProductCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_category(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListAPIView(APIView):
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    def get_product(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_product(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    filter_backends = [SearchFilter]

    search_fields = ['order_status', 'email__email']

    queryset = Order.objects.all()


class OrderCreateAPIView(APIView):
    def get_info(self, data):
        email = data['email']
        pk = data['product']
        amount = data['amount']
        date = datetime.now().strftime("%Y-%m-%d")
        return email, pk, amount, date

    def get_currency(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            currency = product.currency
            return currency
        except Product.DoesNotExist:
            raise Http404

    def get_bill(self, email, pk):
        try:
            currency = self.get_currency(pk)
            bill = Bill.objects.get(email=email, currency=currency)
            return bill
        except Bill.DoesNotExist:
            raise Http404

    def get_cost(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            cost = product.cost
            return cost
        except Product.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)

        if serializer.is_valid():
            email, pk, amount, date = self.get_info(request.data)

            orders = Order.objects.filter(email=email, order_time__contains=date).count()

            bill = self.get_bill(email, pk)
            money = bill.money

            cost = self.get_cost(pk)
            total_cost = cost * amount

            if orders < 5 and total_cost <= money:
                serializer.save()

                data = {'money': money - total_cost}
                bill_serializer = BillSerializer(bill, data=data, partial=True)
                if bill_serializer.is_valid():
                    bill_serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIView(APIView):
    def get_order(self, pk):
        try:
            order = Order.objects.get(pk=pk)
            return order
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_order(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        product = self.get_order(pk)
        data = {'order_status': "Отменённый"}

        serializer = OrderSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillListAPIView(APIView):
    def post(self, request):
        serializer = BillCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Bill.objects.all()
        serializer = BillSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BillAPIView(APIView):
    def get_bill(self, pk):
        try:
            order = Bill.objects.get(pk=pk)
            return order
        except Bill.DoesNotExist:
            raise Http404

    def patch(self, request, pk, money):
        bill = self.get_bill(pk)
        data = {'money': bill.money + money}

        serializer = BillSerializer(bill, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
