from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # calling these two views will let us use the django.
# building login and logout form at registration/login.html,using "template_name" will let us change that directory

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
