from .models import Profile
from rest_framework import serializers





class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ("id" ,"position","Kind","name","num","e_mail","password","score")


