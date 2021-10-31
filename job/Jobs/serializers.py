### get data from model ----> json 

from rest_framework import serializers
from .models import *

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = job 
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
