from django.urls import path
from .views import ContactCreate, thanks

urlpatterns = [
    path("contactform/", ContactCreate.as_view(), name="contactform"),
    path("thanks/", thanks, name="thanks"),
]
