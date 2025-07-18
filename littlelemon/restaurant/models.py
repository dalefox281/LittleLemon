from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(
        default = 1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ]
    )
    Booking_date = models.DateField()

    def __str__(self):
        return f'{self.Name} : {str(self.Booking_date)}'

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
        ]
    )

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
