from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('update<pk>',update,name='update'),
    path('delete<pk>',delete,name='delete')
    
]