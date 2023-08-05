from rest_framework import serializers
from users.models import User

from users.models import User

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        # extra_kwargs = {
        #     "id": {"read_only": True},
        #     "email": {"required": True},
        #     "password": {"required": True},
        # }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

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


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
