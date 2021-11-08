from django.urls import path 
from .views import *

app_name='Jobs'

urlpatterns = [
   path('jobs_list',api_list_job.as_view() ,name="jobs_list"),
   path('jobs_detalis/<slug>' ,api_detail_job.as_view() , name='job_detail'),
   path('jobs_detalis/<slug>/update' , api_edit_job.as_view() , name="update_job"),
   path('jobs_detalis/<slug>/delete' , api_delete_job.as_view() , name="delete_job"),
   path('api_category_create' , api_create_category.as_view() , name="create_category"),
   path('api_job_create' , api_create_job.as_view() , name="api_job_create"),

]
