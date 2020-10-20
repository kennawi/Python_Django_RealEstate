from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

# urlpatterns = [
#     path('i18n/', include('django.conf.urls.i18n')),
#     # path('admin/', admin.site.urls),
#     ]
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    # path('', include('pages.urls')),
    # path('listings/', include('listings.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('contacts/', include('contacts.urls')),
    # path('admin/', admin.site.urls),
    ]
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('contactform/', include('contactform.urls')),

    # prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
