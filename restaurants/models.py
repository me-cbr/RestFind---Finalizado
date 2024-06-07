from django.db import models

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=65)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

class City(models.Model):
    name = models.CharField(max_length=65)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}, {self.state.name}"
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=65)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}, {self.city.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    title = models.CharField(max_length=65)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)    
    description = models.CharField(max_length=255)
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    img_restaurant = models.ImageField(upload_to='restaurant/cover/img', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    
    