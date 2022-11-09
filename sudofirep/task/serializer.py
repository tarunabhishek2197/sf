from rest_framework import serializers
from .models import Customer, User



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "profile_number","user"]
        depth = 1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","first_name", "last_name","email","mobile_no" ]        