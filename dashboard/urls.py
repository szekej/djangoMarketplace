from dashboard.views import index
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='index')
]