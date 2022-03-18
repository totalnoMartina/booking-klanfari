from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from cloudinary.models import CloudinaryField


class Guest(models.Model):
    """
    A model for a Guest/Admin
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.username


class GManager(models.Model):
    """ A model for the one that manages guests and bookings """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'Manager {self.first_name} {self.last_name}'




APARTMENTS = (('Tony', 'Tony Apartment for max4 people'),
                ('Matea', 'Matea apartment for max4 people'),
                ('Martina', 'Martina apartment for max6 people'))
class AppName(models.Model):
    """
    A model for the apartment details
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apartment_name = models.CharField(choices=APARTMENTS, max_length=10, null=False)
    front_image = CloudinaryField('front_image', default='first_img') # cloudinary needs to store this
    front_image2 = CloudinaryField('front_image2', default='second_img') # cloudinary needs to store this
    front_image3 = CloudinaryField('front_image3', default='third_img') # cloudinary needs to store this
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(name='description', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Apartment {self.apartment_name} price: {self.price}'

class AppStatus(models.Model):
    """ Showing the status of the apartment """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        """
        Returns a string representation of the model instance
        """
        return f'Apartment {self.status}'


class Apartment(models.Model):
    """ A model for the apartment status and price details """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    app_name_id = models.ForeignKey(AppName, on_delete=models.CASCADE)
    app_status_id = models.ForeignKey(AppStatus, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'Apartment {self.app_name_id} price:{self.price} is currently {self.app_status_id}'


class PaymentType(models.Model):
    """ A model for the payments """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'Payment option {self.name}'


class Payment(models.Model):
    """ A model for the payments details and guest connected to """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=CASCADE)
    manager_id = models.ForeignKey(GManager, on_delete=CASCADE)
    amount = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Guest {self.guest_id} amount:{self.amount} processed by Manager {self.manager_id}'


class Booking(models.Model):
    """ A model for the booking process """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=CASCADE)
    manager_id = models.ForeignKey(GManager, on_delete=CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Booking by guest {self.guest_id} paid {self.payment_id} for apartment {self.apartment_id}'
