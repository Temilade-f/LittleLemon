from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=225)
    No_of_guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self):
        return self.Name
        
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=225)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.Title} : {str(slef.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.PositiveSmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'