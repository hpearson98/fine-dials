from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Brand(models.Model):
    """
    This is the model for the brands to be associated to the products
    """
    name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
    )
    country_of_origin = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    year_established = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.date.today().year),
        ],
    )

    def __str__(self):
        return self.name


MOVEMENT_CHOICES = (
    ("AUTO", "Automatic"),
    ("QUARTZ", "Quartz"),
)


class Watch(models.Model):
    """
    This is the model to store data for the watches
    """
    brand = models.ForeignKey(
        'Brand',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=40,
    )
    description = models.TextField()
    movement = models.CharField(
        choices=MOVEMENT_CHOICES,
        null=False,
        blank=False,
        max_length=30,
    )
    calibre = models.CharField(
        null=False,
        blank=True,
        max_length=30,
    )
    water_resistance = models.CharField(
        null=False,
        blank=False,
        max_length=5,
    )
    other_features = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.brand + self.model