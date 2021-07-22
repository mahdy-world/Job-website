
from django.urls import path , include
from . import views
from . import api

app_name='Jobs'

urlpatterns = [
   
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>' , views.job_detail,name='job_detail'),

    ## api 
    path('api/jobs/',api.job_list_api , name = 'jobListApi'),
    path('api/jobs/<int:id>',api.job_detail_api , name = 'jobDetailApi'),

    ## class based views 
    path('api/v2/jobs/',api.jobListApi.as_view() , name = 'jobListApi'),
    path('api/v2/jobs/<int:id>/',api.jobDetailApi.as_view() , name = 'jobListApi'),
]
