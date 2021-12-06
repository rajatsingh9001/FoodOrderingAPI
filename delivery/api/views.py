from django.db.models import query
from django.shortcuts import render
from django.utils.module_loading import module_has_submodule
from rest_framework import serializers
from rest_framework import response
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import MenuItems, RestMenuItems, RestaurantList, Customer, Order
from .serializers import  RestListSerializer,RestDetailSerializer,RestDetailSerializer_create,CustomerSerializer
import sys
from datetime import date, datetime
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
SECRET_KEY = 'django-insecure-zg1!oim9keb0^a_^_^f8ygn*@@p&q36co%gabw)fx)#w+78d8)'

# Create your views here.
class RestaurantListView(APIView):
    def post(self,request):
        try:
            data= request.data
            serializer = RestListSerializer(data= data)
            serializer.is_valid(raise_exception= True)
            serializer.save()
            data= {
                    'status': True,
                    'data': serializer.data,
                    'error':None
                    }
            return Response(data)
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            data= {
                'status': False,
                'data': [],
                'error': str(e)
            }
            print(filename,line_number)
            return Response(data)
    
    def get(self,request):
        try:
            data = RestaurantList.objects.all()
            data_serializer = RestListSerializer(data, many = True)
            data ={
                    'status':True,
                    'data': data_serializer.data,
                    'error':None
                    }
            return Response(data)
        except Exception as e:
            return Response(str(e))



class RestaurantDetailView(ModelViewSet):
    queryset = RestaurantList.objects.all()

    serializer_class = RestDetailSerializer
    def create(self,request):
        try:
            data= request.data
            serializer = RestDetailSerializer_create(data= data)
            serializer.is_valid(raise_exception= True)
            serializer.save()
            data= {
                    'status': True,
                    'data': serializer.data,
                    'error':None
                    }
            return Response(data)
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            data= {
                'status': False,
                'data': [],
                'error': str(e)
            }
            print(filename,line_number)
            return Response(data)

    def list(self,request):
        try:
            data = RestaurantList.objects.all()
            data_serializer = RestDetailSerializer(data, many = True)
            data ={
                    'status':True,
                    'data': data_serializer.data,
                    'error':None
                    }
            return Response(data)
        except Exception as e:
            return Response(str(e))

# class MenuItemView(ModelViewSet):
    # queryset = RestMenuItems.objects.all()
    # serializer_class = ItemsSerializer
    # def create(self, request):
    #     email = request.user.email
    #     restaurantId = RestaurantList.objects.get(email=email)
    #     restaurantId = restaurantId.id
        
    

class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self,request):
        try:
            rawData = request.data
            dob = rawData.get('dob').split('-')
            dob = datetime(int(dob[0]),int(dob[1]),int(dob[2]))
            rawData['dob']=dob
            data = rawData
            serializer = CustomerSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {'status': True,
                    'data': serializer.data,
                    'error':None
            }
            return Response(data)
        except Exception as e:
            data = {'status': False,
                    'data': [],
                    'error': str(e)
                    }
            return Response(data)
    def list(self,request):
        try:
            data = Customer.objects.all()
            data_serializer = CustomerSerializer(data, many = True)
            data ={
                    'status':True,
                    'data': data_serializer.data,
                    'error':None
                    }
            return Response(data)
        except Exception as e:
            return Response(str(e))


# class OrderView(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self,request):
#         try:
#             rawData = request.data
#             serializer = OrderSerializer_create(data=rawData)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             data = {'status': True,
#                     'data': serializer.data,
#                     'error':None
#             }
#             return Response(data)
#         except Exception as e:
#             return Response(str(e))


class GetOtpView(APIView):
    def get(self,request):
        return Response({'message': 'OTP sent to '+ request.data.get('phoneno')})
        

class VerifyOtpView(APIView):
    def get(self,request):
        data = request.data
        otp= 123456
        if request.data.get('otp')==otp:
            user = User.objects.create_user(username=data.get('phone'),password=SECRET_KEY)
            user.save()
        data = {
                'status': True,
                'data': str(user),
                'message': 'User created',
                'error': None
            }
        return Response(data)

    def post(self,request):
        token = TokenObtainPairView.as_view()(request._request).data
        data = {
                    'status': True,
                    'message': 'Fill details on next page',
                    'error': None,
                    'token': token
            }
        return Response(data)

class RestMenuItemsView(ModelViewSet):
    queryset = RestaurantList.objects.all()
    serializer_class = RestDetailSerializer
    def retrieve(self, request, *args, **kwargs):
        try:
            data = self.get_object()
            data_serializer = RestDetailSerializer(data)
            items = data_serializer.data.get("menu_list")
            data = {
                'status':True,
                'data':items,
                'error':None
            }
            return Response(data)
        except Exception as e:
            return Response(str(e))

class LoginView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Serializer
    def create(self, request):
        try:
            data= request.data
            user = User.objects.create_user(username=data.get('username'),password=data.get('password'))
            user.save()
            return Response({'status':'user created'})
        except Exception as e:
            return response(str(e))
    
    @action(detail=False,methods =['POST'])
    def restLogin(self, request):
        try:
            data = request.data
            token = TokenObtainPairView.as_view()(request._request).data
            data={
                "status":True,
                'token':token,
            }
            return Response(data)
        except Exception as e:
            return response(str(e))