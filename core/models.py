from django.db import models
from django.contrib.auth import get_user_model
class Shop (models.Model) :
    title = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    create_data = models.DateTimeField()
    what_update = models.DateTimeField()
    #image
# Create your models here.
