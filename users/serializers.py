from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        print(validated_data)
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
