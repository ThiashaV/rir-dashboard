# coding=utf-8
__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '13/10/21'

"""Project level url handler."""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rir/', include('rir_data.urls')),
    url(r'^', include('rir_dashboard.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
