from django.urls import path
from hv_main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('offers', views.offers, name='offers'),
    path('cloud', views.cloud, name='cloud'),
    path('calendar', views.calendar, name='calendar'),
    path('contact', views.contact, name='contact'),
    path('impressum', views.impressum, name='impressum'),
]
