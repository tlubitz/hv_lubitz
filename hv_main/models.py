from django.db import models


# Create your models here.
class DataModel(models.Model):

    title = models.CharField(max_length=100)
    notes = models.CharField(max_length=255)
    f = models.FileField()
    
    def __str__(self):
        return self.title


    def botho(self):
        print('do botho stuff')
        print(self.title)
