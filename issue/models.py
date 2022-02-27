from django.db import models


# Create your models here.
class Issue(models.Model):
    subject = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'Issue'
