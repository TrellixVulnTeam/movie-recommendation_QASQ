from ast import keyword
from turtle import title
from attr import field
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    title=serializers.CharField();
    budget = serializers.IntegerField();
    genres = serializers.CharField();
    keywords = serializers.CharField();
    overview = serializers.CharField();
    tagline = serializers.CharField();
    cast = serializers.CharField();
    director = serializers.CharField();

    class Meta:
        model = Movie
        fields =('id','title','budget','genres','keywords','overview','tagline','cast','director')