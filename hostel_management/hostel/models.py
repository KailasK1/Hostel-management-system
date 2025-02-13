from django.db import models
import uuid

# Room Model
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    is_vacant = models.BooleanField(default=True)
    rent = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {'Vacant' if self.is_vacant else 'Occupied'}"


# User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True, blank=True)
    login_key = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.login_key:  # Set the login_key automatically
            self.login_key = self.name + "123"
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

