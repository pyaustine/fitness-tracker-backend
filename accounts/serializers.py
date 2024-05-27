from accounts.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# register user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        errors = {}
        required_fields = ['email', 'username', 'password', 'password2']
        for field in required_fields:
            if field not in attrs:
                errors['message'] = f"{field} is missing."

        if errors:
            raise serializers.ValidationError(errors)

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"message": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        # Lowercase the email and username before saving it
        validated_data['email'] = validated_data['email'].lower()
        validated_data['username'] = validated_data['username'].lower()

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# login
class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField()

    def validate_email(self, value):
        """
        Normalize the email to lowercase during validation.
        """
        return value.lower()

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Include these in the token payload
        token['email'] = user.email
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        
        # print(token)
        return token

# profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['height', 'weight', 'age', 'fitness_goals']

    def validate(self, data):
        """
        Custom validation to check for positive height and weight
        """
        if 'height' in data and data['height'] <= 0:
            raise serializers.ValidationError("Height must be a positive number.")
        if 'weight' in data and data['weight'] <= 0:
            raise serializers.ValidationError("Weight must be a positive number.")
        return data