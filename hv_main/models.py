from django.db import models

# Create your models here.
class HvModel(models.Model):
    '''
    Our database class which holds the files that need to
    be backed up; preferrably with a cloud hoster (boto?)
    '''
    
    
    def __init__(self, f, file_name):
        self.f = f
        self.file_name = file_name
    
    def __str__(self):
        return self.field_name

    def save(self):
        # boto stuff?
        print('in model')
        print(self.f)
        print(self.file_name)
        pass
