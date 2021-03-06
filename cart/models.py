from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    amount = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.code
