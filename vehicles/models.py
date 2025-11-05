from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    license_plate = models.CharField(max_length=20, unique=True, verbose_name="Госномер")
    is_active = models.BooleanField(default=True, verbose_name="В эксплуатации")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"