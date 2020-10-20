import django_filters
from django.utils.translation import ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import TextInput
from .models import *




class ListingFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(label=_('Keywards'),lookup_expr='icontains', widget=TextInput(attrs={'placeholder':ugettext_lazy('Keywards')}))
	city = django_filters.ChoiceFilter(label=_('City'),choices=Cities)
	category = django_filters.ChoiceFilter(choices=CATEGORIES,label=_('Category'))



	class Meta:
		model = Listing
		fields = ['category','city']
