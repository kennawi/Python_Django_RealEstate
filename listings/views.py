from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.models import CATEGORIES
from listings.choices import price_choices, bedroom_choices, state_choices, category_choices
from django.utils.translation import gettext_lazy as _
from listings.filters import ListingFilter
from listings.models import Listing



def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
 

  listing = Listing.objects.all()
  listing_filter = ListingFilter(request.GET, queryset=listing)

  # myFilters = ListingFilter()
  # Keywords
  # if 'keywords' in request.GET:
  #   keywords = request.GET['keywords']
  #   if keywords:
  #     listing = queryset_list.filter(description__icontains=keywords)

  # City
  # if 'city' in request.GET:
  #   city = request.GET['city']
  #   if city:
  #     queryset_list = queryset_list.filter(city__iexact=city)

  # Category
  # if 'category' in request.GET:
  #   category = request.GET['category']
  #   if category:
  #     queryset_list = queryset_list.filter(category__iexact=category)

  #State
  # if 'state' in request.GET:
  #   state = request.GET['state']
  #   if state:
  #     queryset_list = queryset_list.filter(state__iexact=state)

  #Bedrooms
  # if 'bedrooms' in request.GET:
  #   bedrooms = request.GET['bedrooms']
  #   if bedrooms:
  #     queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  # if 'price' in request.GET:
  #   price = request.GET['price']
  #   if price:
  #     queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'filter': listing_filter,
    # 'state_choices': state_choices,
    # 'category_choices':category_choices,
    # 'bedroom_choices': bedroom_choices,
    # 'price_choices': price_choices,
    'listings': listing,
    # 'values': request.GET,
  }

  return render(request, 'listings/search.html', context)

  # def home(request):
  #   # from django.utils import translation
  #   # user_language = 'ar'
  #   # translation.activate(user_language)
  #   # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
  #   posts = Post.objects.all().order_by('order')
  #   return render(request, 'listings/listings.html', {'posts': posts})
