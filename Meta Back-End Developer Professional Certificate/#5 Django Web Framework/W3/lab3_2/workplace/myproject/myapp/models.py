from django.db import models

# Create your models here.
# Create model DrinksCategory 
class DrinksCategory(models.Model):
    # Define attributes for the class
    # For example:
    category_name = models.CharField(max_length=200)

# Create model Drinks
class Drinks(models.Model):
    # Define attributes for the class
    # For example:
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)
