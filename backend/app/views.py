from django.shortcuts import get_object_or_404, render
from app.models import *
from .seriealizers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

# Create your views here.
#model Object - Single Student Data

def slider_detail(request, pk):
    slid = Slider.objects.get(id= pk)
    serializer = SliderSerializer(slid)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#query set - All Slider Data
def slider_list(request):
    slid = Slider.objects.all()
    serializer = SliderSerializer(slid, many= True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data)
# GEt all Slider 
def get_slider_data(request):
    sliders = Slider.objects.all()
    data = [
        {
            "title": slider.title,
            "image_url": request.build_absolute_uri(slider.image.url),
        }
        for slider in sliders
    ]
    return JsonResponse(data, safe=False)


#post the contact page
class ContactUsCreateView(APIView):
    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# GEt all Slider 
def get_gallery_data(request):
    gallery = Gallery.objects.all()
    data = [
        {
            "name": gallery.name,
            "image_url": request.build_absolute_uri(gallery.image.url),
        }
        for gallery in gallery
    ]
    return JsonResponse(data, safe=False)

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class companyDetails(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerialization