# from django.shortcuts import render
from users.serializers import UserRegistrationSerializer
from rest_framework.views import APIView

# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.serializers import User
from rest_framework import status
from users.admin import User

# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import get_object_or_404


from users.serializers import UserSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
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


from rest_framework import generics


class UserGeneric(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ["username"]
