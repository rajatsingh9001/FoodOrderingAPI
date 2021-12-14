from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import action
from django.contrib.auth.models import User
from models import RestaurantOwner,Order, MenuItems
from serializers import OrderSerializer, OrderSerializer_create, PartnerSerializer, MenuItemsSerializer


class PartnerView(ModelViewSet):
    queryset = RestaurantOwner.objects.all()
    serializer_class = PartnerSerializer
    def create(self,request):
        try:
            data = request.data
            user = User.objects.create_user(username=str(data.get('mobile')),password='password')
            user.save()
            return Response({'status':'user created'})
        except Exception as e:
            return Response(str(e))

class MenuItemsView(ModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
    def list(self, request, *args, **kwargs):
        try:
            data = request.GET.get('restaurant')
            queryset =MenuItems.objects.filter(restaurant=data)
            serializer = MenuItemsSerializer(queryset,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))

class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self,request):
        try:
            rawData = request.data
            serializer = OrderSerializer_create(data=rawData)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {'status': True,
                    'data': serializer.data,
                    'error':None
            }
            return Response(data)
        except Exception as e:
            return Response(str(e))
