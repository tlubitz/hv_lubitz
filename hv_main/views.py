from django.shortcuts import render
from hv_main.models import HvModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def offers(request):
    
    return render(request, 'offers.html')

def impressum(request):
    
    return render(request, 'impressum.html')

@login_required
def cloud(request):
    
    return render(request, 'cloud.html')

@login_required
def calendar(request):
    
    return render(request, 'calendar.html')
