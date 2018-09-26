from django.urls import path
from hv_main import views

urlpatterns = [
    path('', views.index, name='index'),
]
