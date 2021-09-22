from django.db import models

# Create your models here.
class CrudModel(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    phone= models.CharField(max_length=50)
    image = models.ImageField(upload_to='upload_student_image/')
    desc= models.TextField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.desc[0:15]

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    message=models.TextField()

    def __str__(self):
        return self.email


class AboutModel(models.Model):
    aboutimg = models.ImageField( upload_to="aboutImage/")
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50,blank=True)
    occupation = models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.title
    