from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app import views
import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sliderinfo/<int:pk>', views.slider_detail),
    path('sliderinfo/', views.slider_list),
    path('', include('app.urls'))

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 