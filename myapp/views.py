
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# CATEGORY  LIST AND CREATE
@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer( categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED )

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CATEGORY  DETAIL UPDATE AND DELETE
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer( category, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = CategorySerializer(category, data=request.data, partial=True )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )





# PRODUCT LIST AND CREATE
@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.select_related("category").all()
        serializer = ProductSerializer( products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PRODUCT  DETAIL UPDATE AND DELETE
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def product_detail(request, pk):
    product = get_object_or_404(  Product.objects.select_related("category"), pk=pk )
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer( product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = ProductSerializer( product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    elif request.method == "DELETE":
        product.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)