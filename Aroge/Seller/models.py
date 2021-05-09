from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
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
        return "%s, %s, %s" % (self.specific_location, self.city, self.region)


class Seller(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location,  on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,15}$',
        message='Phone number must be entered in the format : 09******** or +2519******** up to 15 digits allowed',
        )
        
    phone = models.CharField(validators=[phone_regex], max_length=15)

    def __str__(self):
        return self.name
 

