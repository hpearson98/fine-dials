from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Brand(models.Model):
    """
    This is the model for the brands to be associated to the products
    """
    name = models.CharField(
        null=False,
        blank=False,
        unique=True,
    )
    country_of_origin = models.CharField(
        null=False,
        blank=False,
    )
    year_established = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(4),
            MaxValueValidator(4),
        ]
    )

