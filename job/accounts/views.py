from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse

# Create your views here.

def signup(request):

    #check request if it == Post 
    if request.method == "POST":
        #store data from request to var calld form
        form = signupForm(request.POST)
        # check form is valid if valid save it in database 
        if form.is_valid:
            form.save()

            # get user name and pass from form to use it in authenticate 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # authenticate using username and pass 
            user = authenticate(username = username , password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = signupForm    

    return render(request,'registration/signup.html' , {'form':form})


def profile(request):
    # get profile for the user he make the request
    profile = Profile.objects.get(user=request.user)
    return render(request , 'accounts/profile.html' , {'profile':profile})    

def profile_edit(request):
    # get profile for the user he make the request
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST" :
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES , instance=profile)

        if userform.is_valid and profileform.is_valid : 
            userform.save()

            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request , 'accounts/profile_edit.html' , {'userform':userform , 'profileform':profileform})


