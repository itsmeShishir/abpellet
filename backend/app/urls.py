from django.urls import include, path
from . import views
from .views import BlogDetail

urlpatterns = [
    path('api/slider/', views.get_slider_data, name='get_slider_data'),
    path('api/contactus/', views.ContactUsCreateView.as_view(), name='contactus-create'),
    path('api/gallery/', views.get_gallery_data, name='get_gallery_data'),
    path('api/blog/', views.BlogList.as_view(), name='blog-list'),
    path('api/blog/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('api/companies/', views.companyDetails.as_view(), name='companies-list'),
    path('api/distributers/', views.DistributersDetails.as_view(), name='distributers-list'),
    path('api/whychooseus/', views.WhyChooseUs.as_view(), name='WhyChooseUs-list'),
    path('api/testimonial/', views.Testimonial.as_view(), name='testimonial-list'),
    path('api/ourpatners/', views.OurPatner.as_view(), name='ourpatners-list'),
    path('api/ourmoto/', views.OurMoto.as_view(), name='ourmoto-list'),
    path('api/teams/', views.Team.as_view(), name='teams-list'),
    path('api/associations/', views.Association.as_view(), name='association-list'),
    path('api/productcategory/', views.ProductCategory.as_view(), name='productcategory-list'),
]