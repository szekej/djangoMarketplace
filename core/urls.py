from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from .views import signup, index, contact

from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', view=contact, name='contact_name'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
