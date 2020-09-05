from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField()


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name = "Название")
    price = models.DecimalField(verbose_name="Цена",decimal_places=2)
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL)

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение")

class ProductTag(models.Model):
    name = models.CharField()


class Customer(User):
    telegram_id = models.IntegerField(unique=True)

class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer, related_name = "customer")



class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderStatus(models.Model):
    state = models.CharField()

class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField()
    qty = models.IntegerField()




