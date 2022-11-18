from django.urls import path 
from core.views import home_view 
from core.views import ProdListView
urlpatterns = [
    path ('', home_view, name = 'home'),
    path ('shop', ProdListView.as_view(), name = 'shop'),
    ]