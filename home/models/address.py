from django.db import models
from django.urls import reverse


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=250)
    unit_number = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.street} {self.unit_number} {self.city} {self.province} {self.postal_code} {self.country}"

    def get_absolute_url(self):
        return reverse("address_details", kwargs={"pk": self.pk})
