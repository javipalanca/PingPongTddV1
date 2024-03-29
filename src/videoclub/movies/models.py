from django.db import models
from rest_framework.compat import MinValueValidator, MaxValueValidator

from videoclub.movies import choices


class Movie(models.Model):
    title = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    genre = models.PositiveSmallIntegerField(null=True, choices=choices.GENRE_CHOICES)
    score = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
