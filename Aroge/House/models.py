from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from Seller.models import Seller
# Create your models here.

region_list = [
    'Addis Ababa', 'Afar', 'Amhara', 'Benishangul-Gumuz', 
    'Dire Dawa', 'Gambela', 'Harari', 'Oromia', 'Sidama', 'Somali', 
    "Southern Nations, Nationalities, and Peoples' Region", 'Tigray'
    ]
region_choice = ((i, i) for i in region_list)
class Location(models.Model):
    region = models.CharField(max_length=100, choices=region_choice)
    city = models.CharField(max_length=1000)
    specific_location = models.CharField(max_length=1000)

    def __str__(self):
        return self.specific_location

class Photo(models.Model):
    image  = models.ImageField(upload_to='images')


class House(models.Model):
    size = models.PositiveIntegerField()
    sell_or_rent = models.CharField(max_length=100, choices=(('Sell', 'Sell'), ('Rent', 'Rent')))
    condition = models.CharField(max_length=100, choices=(('New', 'New'), ('Used', 'Used')))
    house_type = models.CharField(max_length=100)
    bedroom = models.PositiveIntegerField() 
    location = models.ForeignKey(Location,  on_delete=models.CASCADE)
    price =  models.DecimalField(decimal_places=2, max_digits=20,
                                validators=[MinValueValidator(Decimal('0.00'))])
    description = models.TextField(blank=True, null=True)
    photo = models.ManyToManyField(Photo, blank=True)
    seller =  models.ForeignKey(Seller,  on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %f" % (self.sell_or_rent, self.price)
 

