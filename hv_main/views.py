from django.shortcuts import render
from hv_main.models import HvModel
from django.contrib.auth.decorators import login_required

from hv_main.forms import SaveDataForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def offers(request):
    
    return render(request, 'offers.html')

def contact(request):
    
    return render(request, 'contact.html')

@login_required
def cloud(request):
    
    # if this is a POST request then process the Form data
    if request.method == 'POST':
        form = SaveDataForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
            #d = save_data_form.cleaned_data['save_data']
            
            #do what boto tells us to do?

            #return HttpResponseRedirect('/success/url/')
            return HttpResponseRedirect('cloud')
            

    # if the view is called for the first time, we have
    # to initialise it empty(ly)
    else:
        #form = SaveDataForm(initial={'save_data': ''})
        form = SaveDataForm()        

    context = {'form': form}
    
    return render(request, 'cloud.html', context)

@login_required
def calendar(request):
    
    return render(request, 'calendar.html')

def impressum(request):
    
    return render(request, 'impressum.html')
