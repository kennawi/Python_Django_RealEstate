from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.utils.translation import gettext_lazy as _

# from .choices import category_choices


CATEGORIES = (
    (1,_('Apartments')),
    (2,_('Villas')),
    (3,_('Land')),
    (4,_('Commercial'))
)

Cities = (
     (_('Abu Dhabi'), _('Abu Dhabi')),
     (_('Dubai') ,_('Dubai') ),
     (_('Sharjah') , _('Sharjah')),
     (_('Ajman'),_('Ajman')),
     (_('Umm Al Qaiwain'),_('Umm Al Qaiwain')),
     (_('Ras Al Khaimah'),_('Ras Al Khaimah')),
     (_('Fujairah'),_('Fujairah')),
     (_('Other'),_('Other'))
)





class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  category = models.IntegerField(choices=CATEGORIES)
  title = models.CharField(max_length=200)
  # category = models.CharField(max_length=100,choices= category_choices)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100,choices=Cities)
  # state = models.CharField(max_length=100)
  # zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  videofile= models.FileField(upload_to='videos/%Y/%m/%d/', null=True ,blank=True , verbose_name="Vedio")
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
