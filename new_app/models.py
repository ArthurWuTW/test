from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(blank=False, null=False)
    stock_pcs = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    shop_id = models.CharField(max_length=100, null=False)
    vip = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_id)

    class Meta:
        verbose_name_plural = 'Product'

class Order(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    product_id = models.IntegerField(blank=False, null=False)
    qty = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    shop_id = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Order'
