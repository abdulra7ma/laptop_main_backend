from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Items(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)