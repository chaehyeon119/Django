from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True)