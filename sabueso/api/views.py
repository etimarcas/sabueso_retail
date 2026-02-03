from django.shortcuts import render

# Create your views here.
from .models import item
from rest_framework import generics
from .serializers import ItemSerializer

class ItemCreate(generics.CreateAPIView):
     queryset = item.objects.all()
     serializer_class = ItemSerializer

class ItemList(generics.ListAPIView):
     queryset = item.objects.all()
     serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveAPIView):
     queryset = item.objects.all()
     serializer_class = ItemSerializer

class ItemUpdate(generics.RetrieveUpdateAPIView):
     queryset = item.objects.all()
     serializer_class = ItemSerializer     

class ItemDelete(generics.RetrieveDestroyAPIView):
     queryset = item.objects.all()
     serializer_class = ItemSerializer      


# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = item.objects.all()
#     serializer_class = ItemSerializer


