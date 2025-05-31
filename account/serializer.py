from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['profile_image']


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        profile_image = request.FILES.get('profile_image') if request else None

        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)

        Profile.objects.create(user=user, profile_image=profile_image)
        return user
