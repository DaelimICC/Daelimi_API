from django.db import models


# Test Class
class Question(models.Model):
    message = models.CharField(max_length=300)
    isFilter = models.IntegerField()

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'Question'


class Answer(models.Model):
    answer = models.CharField(max_length=300)
