from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Order, MenuItem, DeliveryCrew, Cart
from .serializers import SerializedMenuItem

@api_view(['GET'])
def home(request):
    menu_items = MenuItem.objects.all()
    serialized_menu_items = SerializedMenuItem(menu_items, many=True)
    data = serialized_menu_items.data
    return Response(data, status=status.HTTP_200_OK)


