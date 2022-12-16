from django.urls import path 
from accounts.views import UserCreationView
import django.contrib.auth.views as auth_views
urlpatterns = [
    path ("signup/", UserCreationView.as_view(), name = "signup" ),
    path ("login/", auth_views.LoginView.as_view(), name = "login"),
    path ("logout/", auth_views.LogoutView.as_view(), name = "logout")
]