from django.contrib import admin
from django.urls import path
from .views import signup, index, contact

from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', view=contact, name='contact_name'),
    path('signup/', signup, name='signup')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)