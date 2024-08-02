from django.db import models
from django.utils.text import slugify

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=100,default=1)
    slug=models.SlugField(max_length=250,unique=True,default=1)
    dep_description=models.TextField()

    def save(self,*args, **kwargs):
        if not self.slug:
            # self.slug=self.generate_unique_slug()
            self.slug=slugify(self.dep_name)
        super().save(*args,**kwargs)
    # def generate_unique_slug(self):
    #     slug=slugify(self.dep_name)
    #     unique_slug=slug
    #     counter=1
    #     while Department.objects.filter(slug=unique_slug).exists():
    #         unique_slug=f"{slug}-{counter}"
    #         counter+=1
    #     return unique_slug
    def __str__(self):
        return self.dep_name
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.TextField()
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE,default=1)
    doc_image=models.ImageField(upload_to='doctors',default='default_image.jpg')

    def __str__(self):
         return 'DR'+' '+ self.doc_name
    
class  Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name
    
class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name