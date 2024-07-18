from django.db import models


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
