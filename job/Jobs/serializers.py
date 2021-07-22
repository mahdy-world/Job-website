### get data from model ----> json 

from rest_framework import serializers
from .models import job 

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = job 
        fields = '__all__'