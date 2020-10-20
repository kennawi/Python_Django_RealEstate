from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactForm
from django.urls import reverse_lazy

# Create your views here.


def contactform(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']

    contactform = ContactForm(name=name, email=email, phone=phone, message=message)

    contactform.save()

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return TemplateResponse(request, 'pages\contact_form.html', {})
