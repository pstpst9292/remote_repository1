from django.db import models

class Feedback1Data(models.Model):
    Name=models.CharField(max_length=100)
    Rating=models.IntegerField()
    Mobile=models.BigIntegerField()
    Email=models.EmailField(max_length=100)
    Date=models.DateTimeField()
    feeb=models.TextField(max_length=100)
