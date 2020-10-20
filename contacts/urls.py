from django.urls import path

from . import views

urlpatterns = [
  path('contact/', views.contact, name='contact'),
  path('landing/', views.landing, name='landing'),
  # path('contactform/', views.ContactCreate.as_view(), name='contactform'),
  # path('thanks/', views.thanks, name='thanks'),
]
