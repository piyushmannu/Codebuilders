from django.db import models


# Create your models here.
class about_img(models.Model):
    aimg = models.ImageField(upload_to='images')
    content = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.content

class porfolio(models.Model):
    Gallery = models.ImageField(upload_to='')

class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

class signup(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    