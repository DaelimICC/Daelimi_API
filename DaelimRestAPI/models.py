from django.db import models

# Request Form
# message : Question
# isFilter : Location and FAQ
class Question(models.Model):
    message = models.CharField(max_length=300)
    isFilter = models.IntegerField()

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'Question'


class Facility(models.Model):
    academicBuilding = models.CharField(max_length=50)
    facilityName = models.CharField(max_length=50)
    floor = models.IntegerField()

    def __str__(self):
        return self.facilityName

    class Meta:
        db_table = 'Facility'
