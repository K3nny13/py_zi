from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Tutorial(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512)


class Rating(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'tutorial'),)
        index_together = (('user', 'tutorial'),)
