from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User  # For the user field

from app.models import Associations, Blog, BlogCategory, Companies, ContactUs, Distributers, Gallery, OurPatners, Ourmoto, ProductCategory, Teams, Testimonials, WhyChoose

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
        fields = ['id', 'title', 'description', 'user', 'category_names', 'image','created_at']


class CompanySerialization(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['id', 'name', 'description', 'image']

class DistributersSerialization(serializers.ModelSerializer):
    class Meta:
        model = Distributers
        fields = ['id', 'name', 'description', 'image']
        
class WhyChooseUsSerialization(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = ['id', 'title', 'description']

class TestimonialsSerialization(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ['id', 'name', 'title', 'description', 'image', 'postinCompany']

class OurPatnersSerialization(serializers.ModelSerializer):
    class Meta:
        model = OurPatners
        fields = ['patnerslink', 'image']

class OurmotosSerialization(serializers.ModelSerializer):
    class Meta:
        model = Ourmoto
        fields = ['title', 'description']

class TeamsSerialization(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['name', 'company_position', 'short_description', 'twitter_link', 'image','facebook_link']
        
class AssociationsSerialization(serializers.ModelSerializer):
    class Meta:
        model = Associations
        fields = ['link', 'image']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'  

     