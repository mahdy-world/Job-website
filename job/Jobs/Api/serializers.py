from rest_framework import serializers

from Jobs.models import *



# class JobsSerializers(serializers.ModelSerializer):
#     # we must create those cause forgin key needed it
#     owner_id = serializers.IntegerField(default=0)
#     # title_ = serializers.CharField(default='title')
#     category_id = serializers.IntegerField(default=0)
#     companie_id = serializers.IntegerField(default=0)
#
#     class Meta:
#         model = job
#         fields = "owner_id", \
#                  "title", \
#                  "job_type", \
#                  "discrpations", \
#                  "vacancy", \
#                  "salary", \
#                  "experience", \
#                  "image", \
#                  "category_id", \
#                  "companie_id" , \
#                  "slug"
#
#     # To create forgin key fields
#     def create(self, validated_data):
#         user_id = validated_data.pop('owner_id')
#         owner = User.objects.get(id=user_id)
#
#         category_id = validated_data.pop('category_id')
#         category = Category.objects.get(id=category_id)
#
#         company_id = validated_data.pop('companie_id')
#         companie = Compaine.objects.get(id=company_id)
#
#         # names in database
#         model_instance = job.objects.create(**validated_data, owner=owner, category=category, companie=companie)
#         return model_instance



class JobSerializerList(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField (view_name="job_detail",
    lookup_field="slug")
    class Meta:
        model = job
        fields = "title" , "job_type" , "discrpations"  , "vacancy" , "salary" , "experience" , "image" , "category" , "companie" , "owner" , "slug" , "url"

# Custome serializer For Create Job With Forgin Key This Best Another Above
class JobSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "title" , "job_type" , "discrpations"  , "vacancy" , "salary" ,\
                 "experience" , "image" , "category" , "companie" , "owner" , "slug"



class JobSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "title" , "job_type" , "discrpations"  , "vacancy" , "salary" ,\
                 "experience" , "image" , "category" , "companie" , "owner" , "slug"



class JobSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "title" , "job_type" , "discrpations"  , "vacancy" , "salary" , \
                 "experience" , "image" , "category" , "companie" , "owner" , "slug"


class JobSerializerDelete(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "title" , "job_type" , "discrpations"  , "vacancy" , "salary" ,\
                 "experience" , "image" , "category" , "companie" , "owner" , "slug"




class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Compaine
        fields = '__all__'
