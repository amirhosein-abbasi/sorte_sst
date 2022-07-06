from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('contact_us', contact_us, name='contact_us'),
    path('newsletter', newsletter, name='newsletter'),
]