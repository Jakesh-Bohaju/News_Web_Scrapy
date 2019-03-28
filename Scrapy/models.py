from django.db import models


class NewsScrapy(models.Model):
    title = models.CharField(max_length=200)
    news = models.TextField(blank=True)
    image = models.CharField(max_length=200)
