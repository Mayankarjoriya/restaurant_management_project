from django.db import models

# Create your models here.
class MenuCategory(models.model):
    name = models.CharField(max_length=100, unique=True)

    def__str__(self):
        return self.name