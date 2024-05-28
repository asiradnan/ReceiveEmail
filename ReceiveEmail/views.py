from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
from . import settings
from django.contrib import messages

def home(request):
    if request.method=="POST":
        subject = request.POST['subject']
        body = request.POST['body']
        to = request.POST['to']
        file = request.FILES.get('file',None)
        try:
            email = EmailMessage(subject,body,settings.EMAIL_HOST_USER,[to])
            if file is not None:
                email.attach(file.name, file.read(), file.content_type)
            print(email.send())
            messages.success(request,"The mail is sent successfully!")
        except:
            messages.error(request,"There was an error sending the mail")
        return redirect("/")
    return render(request,"home.html")
    