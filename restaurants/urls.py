from django.urls import path

from . import views
from .views import RestaurantCreateView

app_name = 'restaurants'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('restaurants/', views.home, name='home'),
    path('restaurants/add/', RestaurantCreateView.as_view(), name='add'),
    path('restaurants/<int:id>/', views.restaurant, name='restaurant'),
    path('restaurants/search/', views.search, name="search"),
    # path('get-cities/', views.get_cities, name='get_cities'),
    # path('get-states/', views.get_states, name='get_states'),
    # path('get-neighborhoods/', views.get_neighborhoods, name='get_neighborhoods'),
]