from modeltranslation.translator import translator, TranslationOptions
from .models import Listing

class ListingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Listing, ListingTranslationOptions)
