from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hv_main.forms import DataModelForm
from django.utils import timezone



# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def offers(request):
    
    return render(request, 'offers.html')

def contact(request):
    
    return render(request, 'contact.html')

@login_required
def cloud(request):

    if request.method == 'POST':
        form = DataModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            model_instance.botho()
            
            return redirect('cloud')
    else:
        form = DataModelForm()
        return render(request, "cloud.html", {'form':form})
    

@login_required
def calendar(request):
    
    return render(request, 'calendar.html')

def impressum(request):
    
    return render(request, 'impressum.html')
