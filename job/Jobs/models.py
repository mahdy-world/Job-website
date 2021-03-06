from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User
from accounts.models import Compaine

# Create your models here.

Job_type = (

    ('full time' , 'full time'),
    ('part time' , 'part time'),

)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)
    

class job(models.Model):

    owner = models.ForeignKey(User, related_name ='job_owner', on_delete =models.CASCADE)
    title = models.CharField( max_length=100) 
    job_type = models.CharField(max_length=15, choices=Job_type , null=True)
    discrpations = models.TextField(max_length=1000 , null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1 , null=True)
    salary = models.IntegerField(default=0 , null=True)
    experience = models.IntegerField(default=1 , null=True)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload )
    companie = models.ForeignKey(Compaine, related_name='job_companie', verbose_name="companie name", on_delete=models.CASCADE)

    slug = models.SlugField(blank=True,null=True)



    def save(self,*args,**kwargs):
        self.slug  = slugify(self.title)
        super(job,self).save(*args,**kwargs)
    


    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Apply(models.Model):
   
    job = models.ForeignKey(job, related_name= 'apply_job', on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website =  models.URLField(max_length = 200 ,null=True) 
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
            
        
