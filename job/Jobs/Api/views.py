from Jobs.views import job_detail
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse

from rest_framework import generics



from Jobs.Api.serializers import *
from Jobs.models import *

@api_view(['GET'])
def jobsListApi(request):

    try:
       all_jobs = job.objects.all()
       data = JobsSerializers(all_jobs, many=True).data
       return Response({'data':data})
    except job.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def job_details(request, slug):
    try:
       job_detail = job.objects.get(slug=slug)
    except job.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "GET" : 
        data = JobsSerializers(job_detail).data
        return Response({'data' :data})


@api_view(['PUT'])
def job_update(request, slug):
    try:
       job_detail = job.objects.get(slug=slug)
    except job.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "PUT" : 
        serializer = JobsSerializers(job_detail , data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successfuly"
        return Response({'data' :data})
    return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)    


@api_view(['DELETE'])
def job_delete(request, slug):
    try:
       job_detail = job.objects.get(slug=slug)
    except job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE" : 
        operation = job_detail.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["success"] = "delete faild"    
    return Response(data = data)    


# @api_view(['POST'])
# def api_job_create(request):
#     # if request.method == "POST" : 
#     #     serializer = JobsSerializers(data=request.data)
#     #     data = {}
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         data["success"] = "delete successful"
#     #     else:
#     #         data["success"] = "delete faild"    
#     # return Response(data = data)            
#     return HttpResponse("ahmed")      

class api_create_job(generics.CreateAPIView):
    serializer_class = JobsSerializers

    def get_queryset(self):
        return job.objects.all()
           

@api_view(['POST'])
def api_category_create(request):
   
   if request.method == "POST":
       data={}
       serializer = CategorySerializers( data=request.data)
       if serializer.is_valid():
           serializer.save()
           data["success"] = "Created"
           return Response({'data':data}) 
        
