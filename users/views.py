from django.shortcuts import render
from users.serializers import UserLoginSerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from users.serializers import User
from rest_framework import status
from users.admin import User

from rest_framework.generics import get_object_or_404
from rest_framework import filters
from rest_framework import generics
from users.serializers import UserSerializer

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id"]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "id"

class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully.", "status": True},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"status": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    

from django.core.mail import send_mail
import random
from django.conf import settings
from users.email import send_otp_via_email
from users.serializers import UserVerifySerializer,UserJionSerializer

class UserJoinAPIView(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = UserJionSerializer(data= data)
            
            if serializer.is_valid():
                
                # serializer.save()
                email = User.objects.filter(User)
                if User.objects.filter(email = email).exists():
                    return Response({
                        'status':False,
                        'message':'email is already exists'
                    })

                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status':True,
                    'message':'registraion successfully chek email',
                    'data': serializer.data,
                })
            return Response({
                'status':False,
                'message':'somthing went worng',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)


class UserVerifyAPIView(APIView):
    def post(self,request):
        try:
            data = request.data
            serializers = UserVerifySerializer(data= data)

            if serializers.is_valid():
                email = serializers.data['email']
                otp = serializers.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status':False,
                        'message':'somthing went worng',
                        'data': 'invalid email'
                })
                if not user[0].otp != otp:
                    return Response({
                        'status':False,
                        'message':'somthing went worng',
                        'data': 'worng otp'
                    })
                
                user= user.first()
                user.is_verified = True
                user.save()
                
                return Response({
                    'status':True,
                    'message':'account verified',
                    'data': {},
                })
                    
            return Response({
                'status':False,
                'message':'somthing went worng',
                'data': serializers.errors
            })
        except Exception as e:
            print(e)













