from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    required_articles = models.TextField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
