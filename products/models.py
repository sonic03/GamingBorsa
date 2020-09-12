from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(verbose_name="Adı",max_length=300)
    price=models.CharField(verbose_name="Price",max_length=300)
    productCode=models.CharField(verbose_name="Ürün Kodu",max_length=300)

    def __str__(self):
        return self.name
