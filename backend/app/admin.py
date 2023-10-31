from django.contrib import admin
from .models import OurPatners, Slider,ContactUs, Gallery, BlogCategory, Blog, Companies, Distributers, Associations,AboutPage, ProductCategory, Product, Teams, Testimonials, WhyChoose, Ourmoto, SiteSettings 
from django.utils.html import mark_safe


# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
        list_display = ['title', 'display_image']

        def display_image(self, obj):
            # obj.image.url contains the URL to the image file
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="auto" />')
    
        # Define the column as HTML (safe) to render the HTML content
        display_image.short_description = 'Image'
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
        list_display= ['name', 'email', 'phone', 'message']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display= ['name', 'display_images']

    def display_images(self, obj):
        # obj.image.url contains the URL to the image file
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="auto" />')
    
    display_images.short_description = 'Image'

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
      list_display=['category_name']
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title', 'description','user','category_name', 'display_images']
    def display_images(self, obj):
        # obj.image.url contains the URL to the image file
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="auto" />')
    
    display_images.short_description = 'Image'

admin.site.register(Companies)
admin.site.register(Distributers)
admin.site.register(Associations)
# admin.site.register(Homepage, all_admin)
admin.site.register(OurPatners)
admin.site.register(AboutPage)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Teams)
admin.site.register(WhyChoose)
admin.site.register(Ourmoto)
admin.site.register(SiteSettings)
admin.site.register(Testimonials)
