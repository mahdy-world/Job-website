from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def send_message(request):
   about = Info.objects.first()
   
   if request.method == 'POST':
      subject = request.POST['subject']
      email = request.POST['email']
      message = request.POST['message']

      email_from = settings.EMAIL_HOST_USER
      recipient_list = [email]

      send_mail( subject, message,email_from,recipient_list)
      print(send_mail)
      
   return render(request,'contact/contact.html', {'about':about})