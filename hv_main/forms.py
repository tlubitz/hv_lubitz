import datetime
from django import forms

class SaveDataForm(forms.Form):
    '''
    a class that takes care of saving data from a form to AWS
    '''
    def save(self):
        '''
        are there any validation checks for the uploaded file?
        '''
        # this could be a Field for example:
        # date = forms.DateField(help_text='Hilf mir.')

        # for text:
        f_title = forms.CharField(max_length=50)
        
        # could be even better:
        f = forms.FileField()

        print('SOMETHING')
        print(f_title)
        print(f)
        
        #data_file = self.cleaned_data['data_file']

        # clean

        return f

    
        
