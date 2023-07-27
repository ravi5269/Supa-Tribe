from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from users.serializers import User
from rest_framework import status
from users.models import User

from rest_framework.generics import get_object_or_404
from rest_framework import filters
from rest_framework import generics
from users.serializers import UserSerializer
from users.models import User
from django.conf import settings
from users.email import send_otp_via_mail
from users.serializers import VerifySerializer, UserSerializer


from django.contrib.auth import get_user_model

User = get_user_model()


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id"]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "id"


class UserJoinAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializers = UserSerializer(data=data)

            if serializers.is_valid():
                serializers.save()
                send_otp_via_mail(serializers.data["email"])
                return Response(
                    {
                        "status": True,
                        "message": "Registration successfully check email",
                        "data": serializers.data,
                    }
                )
            return Response(
                {
                    "status": False,
                    "message": "Something went worng",
                    "data": serializers.errors,
                }
            )
        except Exception as e:
            print(e)
        return Response({})


class UserEmailVerifyAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializers = VerifySerializer(data=data)

            if serializers.is_valid():
                email = serializers.data["email"]
                otp = serializers.data["otp"]

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": False,
                            "message": "Email not found",
                            "data": "invalid email",
                        }
                    )
                if not user[0].otp == otp:
                    return Response(
                        {"status": False, "message": "Invalid", "data": "Invalid Otp"}
                    )

                user = user.first()
                user.is_staff = True
                user.active = True
                user.save()

                return Response(
                    {
                        "status": True,
                        "message": "Account Verified Successfully.",
                        "data": {},
                    }
                )

            return Response(
                {
                    "status": 500,
                    "message": "somthing went worng",
                    "data": serializers.errors,
                }
            )
        except Exception as e:
            print(e)
        return Response({})
