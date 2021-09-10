from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(primary_key=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField("Название", max_length=50)
    text = models.TextField("Описание")
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'Товар'

    def __str__(self):
        return self.title


