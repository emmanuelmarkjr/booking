from rest_framework import serializers
from .models import UsersPhone, MoviesPerformances, Movies


class UsersPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPhone
        fields = ('phone', )

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class MoviesPerformancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesPerformances
        fields = '__all__'
