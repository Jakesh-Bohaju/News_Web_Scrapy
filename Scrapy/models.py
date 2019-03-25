from django.db import models


class TheodoTeam(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    fun_fact = models.TextField(blank=True)

    class Meta:
        verbose_name = "theodo UK team"


class NewsScrapy(models.Model):
    title = models.CharField(max_length=200)
    news = models.TextField(blank=True)
