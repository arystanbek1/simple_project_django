from django.db import models


class Category(models.Model):
    name = models.CharField("Название продукта", max_length=50)
    count = models.IntegerField("количество продукта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField("Название продукта", max_length=50)
    price = models.PositiveIntegerField("Цена продукта")
    count = models.PositiveIntegerField("Количество продукта")
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, verbose_name="Мясо", related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

