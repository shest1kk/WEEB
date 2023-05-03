from django.contrib.auth.models import User
from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class CarCategories(models.Model):
    nameCategory = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nameCategory}"


class Car(models.Model):
    category = models.ForeignKey(CarCategories, on_delete=models.CASCADE, verbose_name='category')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    license_plate = models.CharField(max_length=12)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Автомобиль бренда: {self.brand}, модели: {self.model}, с номером: {self.license_plate} для категории: {self.category}"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Автомобиль {self.car} арендован {self.renter} за {self.price}"


class PaymentMethod(models.Model):
    method = models.CharField(max_length=30)

    def __srt__(self):
        return {self.method}


class Payment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f"Оплата на сумму {self.amount} за аренду ({self.rental})"
