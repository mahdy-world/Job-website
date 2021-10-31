## views like web  but this for js

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs = job.objects.all()
    data = JobSerializers(all_jobs , many=True).data
    return Response({'data' : data}) 

@api_view(['GET'])
def category_list(request):
    all_category =  Category.objects.all()
    data = CategorySerializers(all_category,many=True).data
    return Response({'data':data})   

@api_view(['GET'])
def job_detail_api(request , id):
    job_detail = job.objects.get(id=id)
    data = JobSerializers(job_detail).data
    return Response({'data':data})

class jobListApi(generics.ListAPIView):
    model = job
    queryset = job.objects.all()
    serializer_class = JobSerializers

class jobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializers
    lookup_field = 'id'        