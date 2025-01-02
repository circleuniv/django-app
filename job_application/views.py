import os
from django.shortcuts import render
from .common import  ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from mysite import  settings

def index(request):
    if request.method == 'POST':
        form=ApplicationForm(request.POST) # call a customer-class
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            date=form.cleaned_data['date']
            occupation=form.cleaned_data['occupation']

            # create data to table
            Form.objects.create(first_name=first_name,last_name=last_name,
                                email=email,date=date,occupation=occupation)
            #send email
            message_body=f"A new job application was submitted. Thank you, {first_name}."
            subject='Form submission confirmation'
            email_message=EmailMessage(subject,message_body,to=[email])
            email_message.send()

            #show message in front-end
            messages.success(request,"Form submitted successfully!")

    return render(request,'index.html')

def tutorial(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path)
    context = {"images": img_list}
    return render(request, 'tutorial.html', context)