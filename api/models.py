from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=12.5)

    @property
    def sale_price(self):
        return '%.2f' % (float(self.price) * 0.8)

    def discount_price(self):
        return '%.2f' % (float(self.price) * 0.95)
