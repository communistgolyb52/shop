from django.shortcuts import render
from core.models import Shop 
from django.views.generic import ListView
def home_view (request) :
    return render(request, "home.html")
# Create your views here.
class ProdListView (ListView) :
    #для каждой категории нужен будет свой класс 
    model = Shop    
