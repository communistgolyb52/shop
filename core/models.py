from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
class Shop (models.Model) :
    title = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    create_data = models.DateTimeField(auto_now_add = True)
    what_update = models.DateTimeField(auto_now = True)
    image = models.ImageField(blank = True)
    slug = models.SlugField(blank = True, unique = True)
    def get_absolute_url (self) :
        return reverse("prod_detail", args = [self.slug])

# Create your models here.
