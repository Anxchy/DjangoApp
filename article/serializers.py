from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #if you want to show specific fields
        fields = ['id','author', 'title', 'email']
        #if you want to show all fields
        #fields= '__all__'



