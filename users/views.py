# from django.shortcuts import render
from users.serializers import UserLoginSerializer
from rest_framework.views import APIView

# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.serializers import User
from rest_framework import status
from users.admin import User

# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from rest_framework import generics

from users.serializers import UserSerializer


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


class UserAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)

            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(
            {"message": "Success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        else:
            return Response({"message": "Data not found", "data": serializer.errors})

    def patch(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        else:
            return Response({"message": "Data not found", "data": serializer.errors})

    def delete(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(
            {"message": "Success", "status": True},
            status=status.HTTP_204_NO_CONTENT,
        )


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "id"


class UserFilterAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id"]


# class LoginSms(models.Model):
#     # result = models.PositiveIntegerField()


#     def __str__(self):
#         return str(self.result)

#     def save(self, *args, **kwargs):
#         # if self.result < 100:
#         account_sid = "AC9481d0154f00421ecd501e36d5910001"
#         auth_token = "fb49313eb16e2d9639b3d8ab1e99f621"
#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             body="+917869144369", from_="+12345163703", to="+917869144369"
#         )

#         print(message.sid)
#         return super().save()
