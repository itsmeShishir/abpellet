from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User  # For the user field

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)  # Make it optional
    message = models.TextField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name
    
class BlogCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Companies(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to="companies/")

    def __str__(self):
        return self.name

class Distributers(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="distributers/")

    def __str__(self):
        return self.name

class Associations(models.Model):
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='associations/')

    def __str__(self):
        return self.link

class Teams(models.Model):
    name = models.CharField(max_length=100)
    company_position = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    twitter_link = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='associations/')

    def __str__(self):
        return self.name

class AboutPage(models.Model):
    messagetitle = models.CharField(max_length=100)
    messagedescription = models.TextField(max_length=250)
    image = models.ImageField(upload_to='about/')
    whowearetitle = models.CharField(max_length=50)
    businessnumber = models.CharField(max_length=20)
    workers = models.CharField(max_length=100)
    farmers = models.CharField(max_length=100)
    whowearedescription = models.TextField(max_length=300)
    historytitle = models.TextField(max_length=100)
    historydescription   = models.TextField(max_length=300)
    # class Meta:
    #     permissions = [
    #         ("can_update_restricted_model", "Can update restricted model"),
    #     ]

    # def save(self, *args, **kwargs):
    #     if self.pk is not None:
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.messagetitle

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='productcategory/')
    internalimage = models.ImageField(upload_to='productcategory/')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    image = models.ImageField(upload_to='Product_images/')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class OurPatners(models.Model):
    patnerslink = models.CharField(max_length=100)
    image = models.ImageField(upload_to='associations/')

    def __str__(self):
        return self.patnerslink

class WhyChoose(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Check if there are already four items in the database
        if WhyChoose.objects.count() >= 4:
            raise ValidationError("You cannot create more than 4 items for WhyChoose.")

        super(WhyChoose, self).save(*args, **kwargs)

class Ourmoto(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    name = models.CharField(max_length=100)
    mainimage = models.ImageField(upload_to="site/images/")
    metakeywords= models.CharField(max_length=100)
    matedescription = models.CharField(max_length=100)
    faviccon = models.ImageField(upload_to="sites/favicon/")
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fb = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/images/")
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    postinCompany = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    