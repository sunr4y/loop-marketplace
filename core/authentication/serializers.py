from rest_framework import serializers


from .models import CustomUser


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True)
    profile_type = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        # Eliminar el campo profile_type si existe
        profile_type = validated_data.pop("profile_type", None)
        print(profile_type)
        return super().create(validated_data), profile_type
