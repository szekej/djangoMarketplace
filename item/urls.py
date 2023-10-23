from django.contrib import admin
from django.urls import path
from .views import detail, new, delete, edit

from django.conf import settings
from django.conf.urls.static import static

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('new_item/', new, name='new'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
