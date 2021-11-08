from Jobs.Api.serializers import *
from Jobs.models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter , OrderingFilter
from .pagination import PostPageNumberPagination , PostLimitOffsetPagination

from rest_framework.permissions import IsAuthenticated , AllowAny , IsAuthenticatedOrReadOnly , IsAdminUser


# @api_view(['GET'])
# def jobsListApi(request):

#     try:
#        all_jobs = job.objects.all()
#        data = JobsSerializers(all_jobs, many=True).data
#        return Response({'data':data})
#     except job.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

# # @api_view(['GET'])
# def job_details(request, slug):
#     try:
#        job_detail = job.objects.get(slug=slug)
#     except job.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

#     if request.method == "GET" : 
#         data = JobsSerializers(job_detail).data
#         return Response({'data' :data})


# @api_view(['PUT'])
# def job_update(request, slug):
#     try:
#        job_detail = job.objects.get(slug=slug)
#     except job.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

#     if request.method == "PUT" : 
#         serializer = JobsSerializers(job_detail , data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "Update Successfuly"
#         return Response({'data' :data})
#     return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)    


# @api_view(['DELETE'])
# def job_delete(request, slug):
#     try:
#        job_detail = job.objects.get(slug=slug)
#     except job.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "DELETE" : 
#         operation = job_detail.delete()
#         data = {}
#         if operation:
#             data["success"] = "delete successful"
#         else:
#             data["success"] = "delete faild"    
#     return Response(data = data)    

# List ALl job API 
class api_list_job(generics.ListAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializerList
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ['title' , 'owner' , 'job_type']
    pagination_class = PostPageNumberPagination
# Create Job API
class api_create_job(generics.CreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializerCreate
    permission_classes = [IsAuthenticated ]

    # To Associate User : the owner who make a request
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)


# View Job detail API    
class api_detail_job(generics.RetrieveAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializerDetails
    permission_classes = [IsAuthenticated ]
    # this because i use slug
    lookup_field = 'slug'


# Edit Job APi 
class api_edit_job(generics.RetrieveUpdateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializerUpdate
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]


    # to add delete button in that page 
    def delete(self,request,slug):
        queryset = get_object_or_404(job,slug=slug)
        queryset.delete()

# Delete Job
class api_delete_job(generics.DestroyAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializerDelete
    lookup_field = 'slug'
# Create Category API


class api_create_category(generics.CreateAPIView):
    serializer_class = CategorySerializers
    def get_queryset(self):
        return Category.objects.all()



# @api_view(['POST'])
# def api_category_create(request):
   
#    if request.method == "POST":
#        data={}
#        serializer = CategorySerializers( data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            data["success"] = "Created"
#            return Response({'data':data}) 
        
