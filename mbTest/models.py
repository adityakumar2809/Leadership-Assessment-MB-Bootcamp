from django.db import models

# Create your models here.


class MBResponse(models.Model):

    name = models.CharField(max_length=255)
    
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    average_score = models.FloatField()
    quadrant = models.IntegerField()

    def __str__(self):
        return self.name