from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2024,
        validators=[MaxValueValidator(2025), MinValueValidator(2015)],  # noqa: E501
    )
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation
