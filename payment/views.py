# Create your views here.

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Items
from .serializers import ItemsSerializer


@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response({"items": serializer.data})
    if request.method == 'POST':
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, id):

    try:
        item = Items.objects.get(pk=id)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemsSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ItemsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
