from rest_framework import serializers
from enroll_app.models import User_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_model
        fields="__all__"