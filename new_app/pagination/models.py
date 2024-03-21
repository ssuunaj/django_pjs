from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self) -> str:
        return self.name