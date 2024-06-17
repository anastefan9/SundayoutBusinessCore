from django.db import models
from authenticationBusiness.models import User

priceRange = (
    ("AFD", "Affordable"),
    ("MRG", "Mid-Range"),
    ("GRM", "Gourmet"),
    ("REF", "Refined"),
    ("LVH", "Lavish")
)

class Business(models.Model):
    businessId = models.AutoField(primary_key=True)
    adminId = models.ForeignKey(User, on_delete = models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length = 100)
    latitude = models.DecimalField(max_digits = 8, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 6)
    score = models.DecimalField(max_digits = 3, decimal_places = 1)
    priceRange = models.CharField(max_length=20, choices=priceRange, default="MRG")
    image = models.ImageField(upload_to="images/")
