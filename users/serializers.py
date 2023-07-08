from rest_framework import serializers
from users.models import User

# serializers.py

# from rest_framework import serializers
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, instance, validated_data):
        password = validated_data.get("password", instance.password)
        if password:
            instance.set_password(password)
            instance.save()
            return instance

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.get("password", instance.password)
        if password:
            instance.set_password(password)
        instance.username = validated_data.get("username", instance.username)
        instance.name = validated_data.get("name", instance.name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.bio = validated_data.get("Bio", instance.bio)
        instance.image = validated_data.get("image", instance.image)
        instance.city = validated_data.get("City", instance.city)
        instance.state = validated_data.get("State", instance.state)
        instance.country = validated_data.get("Country", instance.country)

        instance.save()

        return instance
