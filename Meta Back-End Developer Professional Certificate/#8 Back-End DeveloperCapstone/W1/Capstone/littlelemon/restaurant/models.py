from django.db import models
from django.core.validators import MaxValueValidator
from decimal import Decimal


class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    BookingDate = models.DateTimeField()
    class Meta:
        app_label = 'restaurant'


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        # Ensure price is treated as a Decimal for consistent handling
        price = Decimal(self.price)
        # Format price as a string without trailing zeros if it's an integer value
        price_str = f"{price:.2f}".rstrip('0').rstrip('.') if price == price.to_integral_value() else f"{price:.2f}"
        return f"{self.title} : {price_str}"

