from django.shortcuts import redirect, render
from .forms import signupForm
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)

        if form.is_valid:
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username , password=password)
            login(request,user)
            return redirect('accounts/profile')
    else:
        form = signupForm    

    return render(request,'registration/signup.html' , {'form':form})