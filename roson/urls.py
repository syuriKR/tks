from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('menu',views.menu,name='menu'),
    path('gacha/price',views.pricegacha,name='pricegacha'),
    path('gacha/calorie',views.caloriegacha,name='caloriegacha'),
    path('simulator',views.simulator,name='simulator'),
    path('sim_result',views.sim_result,name='sim_result')
]