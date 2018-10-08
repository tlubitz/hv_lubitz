import datetime
from django import forms

class SaveDataForm(forms.Form):
    '''
    a class that takes care of saving data from a form to AWS
    '''
    def clean_data_file(self):
        '''
        are there any validation checks for the uploaded file?
        '''
        data_file = self.cleaned_data['data_file']

        # clean

        return data_file

    
        
