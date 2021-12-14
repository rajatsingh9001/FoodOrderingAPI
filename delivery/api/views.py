from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RestaurantList
from .serializers import RestDetailSerializer
from rest_framework.response import Response
import sys
from rest_framework.decorators import action
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import SlidingToken,AccessToken
from django.contrib.auth.models import User


class RestaurantDetailView(ModelViewSet):
    queryset = RestaurantList.objects.all()

    serializer_class = RestDetailSerializer
    def create(self,request):
        try:
            data= request.data
            serializer = RestDetailSerializer(data= data)
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


    @action(detail=False, methods=['POST'])
    def signup(self,request):
        phone = request.data.get('mobile')
        user = User.objects.get(username= str(phone))
        return Response(str(AccessToken.for_user(user)))