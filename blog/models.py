from django.db import models

# Create your models here.
class BLOG(models.Model):
    Title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    def __str__(self) -> str:
        return self.Title