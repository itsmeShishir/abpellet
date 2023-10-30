from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User  # For the user field

from app.models import Blog, BlogCategory, ContactUs, Gallery

class SliderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField(max_length=None, use_url=True, read_only=True)

     
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'category_name'] 
    
class BlogSerializer(serializers.ModelSerializer):
    category_names = CategorySerializer(source='category_name', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'user', 'category_names', 'image',]