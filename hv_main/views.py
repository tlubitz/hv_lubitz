from django.shortcuts import render
from hv_main.models import HvModel

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def offers(request):
    
    return render(request, 'offers.html')

def impressum(request):
    
    return render(request, 'impressum.html')
