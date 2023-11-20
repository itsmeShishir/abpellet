from django.urls import include, path
from . import views
from .views import BlogDetail, CategoryDetail, ProductDetail, ProductListByCategory

urlpatterns = [
    path('api/slider/', views.get_slider_data, name='get_slider_data'),
    path('api/contactus/', views.ContactUsCreateView.as_view(), name='contactus-create'),
    path('api/gallery/', views.get_gallery_data, name='get_gallery_data'),
    path('api/blog/', views.BlogList.as_view(), name='blog-list'),
    path('api/blog/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('api/companies/', views.companyDetails.as_view(), name='companies-list'),
    path('api/distributers/', views.DistributersDetails.as_view(), name='distributers-list'),
    path('api/whychooseus/', views.WhyChooseUs.as_view(), name='WhyChooseUs-list'),
    path('api/sitesetting/<int:pk>/', views.SiteSetting.as_view(), name='SiteSetting-list'),
    path('api/testimonial/', views.Testimonial.as_view(), name='testimonial-list'),
    path('api/ourpatners/', views.OurPatner.as_view(), name='ourpatners-list'),
    path('api/ourmoto/', views.OurMoto.as_view(), name='ourmoto-list'),
    path('api/teams/', views.Team.as_view(), name='teams-list'),
    path('api/associations/', views.Association.as_view(), name='association-list'),
    path('api/productcategory/', views.ProductCategoryList.as_view(), name='productcategory-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/categories/<int:category_id>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('api/product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/aboutpage/<int:pk>', views.AboutPages.as_view(), name='aboutpage-list'),
]