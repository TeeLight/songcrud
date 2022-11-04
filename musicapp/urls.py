from django.urls import path 
from .views import *

urlpatterns = [
    path('artistes', artiste_list),
    path('', song_list),
    path('song/<int:id>', song_detail),
]
