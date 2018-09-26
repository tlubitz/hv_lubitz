from django.urls import path
from hv_main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('offers', views.offers, name='offers'),
    path('impressum', views.impressum, name='impressum'),
]
