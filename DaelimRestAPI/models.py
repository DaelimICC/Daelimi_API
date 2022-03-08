from django.db import models

# Request Form
# message : Question
# isFilter : Location and FAQ
class Question(models.Model):
    message = models.CharField(max_length=3000)
    isFilter = models.IntegerField()

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'Question'
