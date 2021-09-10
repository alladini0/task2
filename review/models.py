from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

RATING_CHOICES = [

    (1, 1),

    (2, 2),

    (3, 3),

    (4, 4),

    (5, 5),
    ]


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Рассмотрение'

    def __str__(self):
        return self.text
