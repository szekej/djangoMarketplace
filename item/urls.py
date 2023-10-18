from django.contrib import admin
from django.urls import path
from .views import detail

from django.conf import settings
from django.conf.urls.static import static

app_name = 'item'

urlpatterns = [
    path('<int:pk>', detail, name='detail'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
