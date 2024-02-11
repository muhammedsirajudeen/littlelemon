from django.db import models

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateField()

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    inventory = models.IntegerField()
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'