from django.shortcuts import redirect, render
from Jobs.models import job
from accounts.models import Profile , Compaine

# Create your views here.
def index(request):
    # Get all profile and rutern just 8 
    profile = Profile.objects.all()
    
    # Get all copmanies and return 4

    com = Compaine.objects.all()[0:4]

    # Get all jobs and return just 4 
    some_jobs = job.objects.all()[0:4]
    
    if request.method == 'GET' and request.GET.get('Software'):
        jobs = job.objects.filter(category=2)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})

    if request.method == 'GET' and request.GET.get('Design'):
        jobs = job.objects.filter(category=1)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})


    if request.method == 'GET' and request.GET.get('Markting'):
        jobs = job.objects.filter(category=3)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})


    if request.method == 'GET' and request.GET.get('Telemarketing'):
        jobs = job.objects.filter(category=4)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})

      
    if request.method == 'GET' and request.GET.get('Engineering'):
        jobs = job.objects.filter(category=5)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})       
        

    if request.method == 'GET' and request.GET.get('Teaching'):
        jobs = job.objects.filter(category=6)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})       
            

    if request.method == 'GET' and request.GET.get('Administration'):
        jobs = job.objects.filter(category=7)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})     


    if request.method == 'GET' and request.GET.get('Garments'):
        jobs = job.objects.filter(category=8)
        all_job = jobs

        return render(request,'job_list.html' , {'all_job':all_job})        

                                                                
    return render(request,'home.html', {'some_jobs':some_jobs , 'profile':profile , 'companie':com})


