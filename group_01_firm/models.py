from django.db import models

# Create your models here.
class Firm(models.Model):
    name = models.CharField(max_length=100)
    cpm = models.CharField(max_length=100)
    investment = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name