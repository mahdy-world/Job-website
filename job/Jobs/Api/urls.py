from django.urls import path 
from .views import *

app_name='Jobs'

urlpatterns = [
   path('jobs_list',jobsListApi ,name="jobs_list"),
   path('jobs_detalis/<slug>' ,job_details , name="job_details_job"),
   path('jobs_detalis/<slug>/update' , job_update , name="update_job"),
   path('jobs_detalis/<slug>/delete' , job_delete , name="delete_job"),
   path('category_create_api' , api_category_create , name="create_category"),
   path('api_job_create' , api_create_job.as_view() , name="api_job_create"),

]
