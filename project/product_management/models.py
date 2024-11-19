from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Additional image field 2
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Additional image field 3
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    orders = models.PositiveIntegerField(default=0)  # Number of orders for the product
    rates = models.FloatField(default=0.0)  # Rating for the product
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
