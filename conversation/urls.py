from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import new_conversation

from django.conf import settings
from django.conf.urls.static import static

app_name = 'conversation'

urlpatterns = [
    path('new_conversation/<int:item_pk>/', new_conversation, name='new_conversation'),

]
