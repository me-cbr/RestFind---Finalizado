from django.urls import path

from . import views
from .views import RestaurantCreateView

app_name = 'restaurants'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('restaurants/', views.home, name='home'),
    path('restaurants/add/', RestaurantCreateView.as_view(), name='add'),
]