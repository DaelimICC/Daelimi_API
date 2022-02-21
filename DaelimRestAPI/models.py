from django.db import models


# Test Class
class Answer(models.Model):
    answer = models.CharField(max_length=300)
    