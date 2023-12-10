from django.db import models
from django.contrib.auth.models import User
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


GENDER_CHOICES = (
    ("MENS", "Men's"),
    ("WOMENS", "Woman's"),
)

STYLE_CHOICES = (
    ("DIVER", "Diver"),
    ("DRESS", "Dress"),
    ("CHRONOGRAPH", "Chronograph"),
    ("PILOT/FIELD", "Pilot/Field"),
    ("GMT", "GMT"),
    ("CASUAL", "Casual"),
    ("DIGITAL", "Digital"),
)

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
    gender = models.CharField(
        choices=GENDER_CHOICES,
        null=False,
        blank=False,
        max_length=10,
        default="",
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=40,
    )
    style = models.CharField(
        choices=STYLE_CHOICES,
        null=False,
        blank=False,
        max_length=30,
        default="",
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
    crystal = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        default=""
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

    class Meta:
        verbose_name_plural = 'Watches'

    def __str__(self):
        return f"{self.brand} {self.model}"


class Review(models.Model):
    watch = models.ForeignKey(Watch, related_name='reviews' ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False, max_length=50)
    body = models.TextField(null=False, blank=False, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title