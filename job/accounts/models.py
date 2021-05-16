from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50 , verbose_name='الاسم')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField( upload_to='profile/')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='user_city',  null=True , blank=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


## create empty profile when user sign up >> using signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)





