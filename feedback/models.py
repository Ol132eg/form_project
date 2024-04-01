from django.db import models
from django.core.validators import MinLengthValidator

class Feedback(models.Model):
    name=models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname=models.CharField(max_length=60)
    feedback=models.TextField()
    rating = models.PositiveBigIntegerField()
# Create your models here.
