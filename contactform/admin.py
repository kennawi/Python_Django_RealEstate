from django.contrib import admin
from .models import ContactForm
# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
  list_display = ('id', 'name','email','phone','contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email','phone')
  list_per_page = 25

admin.site.register(ContactForm,ContactFormAdmin)
