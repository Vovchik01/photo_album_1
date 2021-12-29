from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('view_photo/<str:pk>/', view_photo, name='view_photo'),
    path('add_photo/', add_photo, name='add_photo'),
]
