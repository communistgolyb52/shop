from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import UserSignUpForm
class UserCreationView (CreateView) :
    form_class = UserSignUpForm 
    succes_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

# Create your views here.
