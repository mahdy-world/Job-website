from django.db.models import fields
from rest_framework import serializers
from Jobs.models import * 

class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'
    
