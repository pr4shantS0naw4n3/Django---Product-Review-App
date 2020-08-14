from django.db import models


# Create your models here.
class review(models.Model):
    productId = models.CharField(max_length=20, default='null', blank=False)
    userId = models.CharField(max_length=255, default='null', blank=False)
    profileName = models.CharField(max_length=255, default='null', blank=False)
    helpfulness = models.CharField(max_length=10, default='null', blank=False)
    score = models.FloatField(default=0.0, blank=False)
    time = models.CharField(max_length=20,blank=False, editable=False)
    summary = models.TextField(default='null', blank=False)
    text = models.TextField(default='null', blank=False)
