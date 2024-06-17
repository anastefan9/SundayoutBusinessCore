from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'email', 'password', 'role', 'createdAt')
        read_only_fields = ('createdAt',)

    def create(self, validated_data):
        user = User(
            firstName = validated_data['firstName'],
            lastName = validated_data['lastName'],
            email = validated_data['email'],
            role = validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user