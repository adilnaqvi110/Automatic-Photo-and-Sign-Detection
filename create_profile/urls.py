from django.urls import path
from . import views

app_name = 'create_profile'

urlpatterns = [

    path('', views.create_profile, name='create_profile'),
    path('show_card/<str:pk>', views.show_card, name='show_card'),
    path('card_temp/', views.card_temp, name='card_temp')
 
]