from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider_images/', blank=False)


class Product(models.Model):
    productName = models.CharField(max_length=30)
    Brand = models.CharField(max_length=50)
    Material = models.CharField(max_length=150)  # Corrected max_length
    Color = models.CharField(max_length=30)
    Item_Weight = models.DecimalField(
        max_digits=10, decimal_places=2)  # Corrected field type
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='catagorybag/', blank=False)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.productName


class SpecialProduct(models.Model):
    productName = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='catagorybag/', blank=False)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.productName


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

# Save the Customer profile when the User is saved


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    if hasattr(instance, 'customer'):
        instance.customer.save()


def __str__(self):
    return self.user.username


class Invoice(models.Model):
    # Link the invoice to a customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
