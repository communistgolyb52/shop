from django.shortcuts import render
from core.models import Shop 
from django.views.generic import ListView, DetailView
def home_view (request) :
    return render(request, "home.html")
# Create your views here.
class ProdListView (ListView) :
    #для каждой категории нужен будет свой класс 
    template_name = 'core/prod_list.html'
    model = Shop    
    context_object_name = 'prod_list'
class ProdDetailView (DetailView) :
    model = Shop
    context_object_name = 'product'
    template_name = 'core/prod_detail.html'