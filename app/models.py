from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('AD', 'ادویه جات'),
    ('DM', 'دمنوش'),
    ('AR', 'عرقیجات'),
    ('RO', 'روغن'),
    ('SB', 'سبزیجات خشک')
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    discounted_price = models.DecimalField(default=0, decimal_places=0, max_digits=12, null=True, blank=True)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
