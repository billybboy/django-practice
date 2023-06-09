from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default = 'hello world')

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id})   #f"/products/{self.id}/"