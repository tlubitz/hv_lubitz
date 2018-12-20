#from django import forms
#from hv_main.models import HvModel
from django.forms import ModelForm
from hv_main.models import DataModel

class DataModelForm(ModelForm):
    class Meta:
        model = DataModel
        fields = ['title', 'text', 'notes']

    def boost_botho():
        print('boost')

'''
class SaveDataForm(forms.Form):

    def save(self):
        f = forms.FileField()
        file_name = forms.CharField(max_length=50, required="False", initial="Dateiname eingeben", help_text="Bitte einen Namen für die Datei eingeben, ansonsten wird der originale Dateiname verwendet.")

        print('in forms')
        print(file_name)
        print(self.cleaned_data)
        #pp = self.cleaned_data['file_name']
        #print(pp)
        
        # create database (cloud) record
        new_data_record = HvModel(f, file_name)
        new_data_record.save()
        

        return f

    def clean_file_name(self):

        file_name = self.cleaned_data['file_name']

        # clean
        # if file_name is crappy: raise ValidationError(_('This is crappy!'))
        
        return file_name
'''
        
