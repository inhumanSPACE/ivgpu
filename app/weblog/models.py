from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
