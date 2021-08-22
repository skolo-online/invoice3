
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

from invoice import views as invoice_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #INVOICE URLS
    path('', invoice_views.index, name='index'),
    path('invoice/',include('invoice.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
