from django.urls import path

from . import views

urlpatterns = [
  path('', views.contactform, name='contactform'),

]
