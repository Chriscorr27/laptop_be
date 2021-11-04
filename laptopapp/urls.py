
from django.urls import path
from .views import *

urlpatterns = [
    path('get_laptops/', get_laptop),
    path('get_orders/', get_orders),
    path('create_orders/', create_orders),
    path('get_ip/', get_ip),
]
