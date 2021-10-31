from django.urls import path 
from .views import *

app_name='Jobs'

urlpatterns = [
   path('jobs_list',jobsListApi ,name="jobs_list"),
   path('jobs_detalis/<slug>' ,job_details , name="job_details"),
   path('jobs_detalis/<slug>/update' , job_update , name="update"),
   path('jobs_detalis/<slug>/delete' , job_delete , name="delete"),
   path('jobs_create' , job_create , name="create"),

]
