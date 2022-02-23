from django.db import models


# Test Class
class Question(models.Model):
    message = models.CharField(max_length=300)
    isFilter = models.IntegerField()


class Answer(models.Model):
    answer = models.CharField(max_length=300)
