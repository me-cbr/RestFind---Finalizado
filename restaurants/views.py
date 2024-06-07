import os
from django.http import JsonResponse

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import RestaurantForm

def dashboard(request):
    return render(request, 'restaurants/pages/dashboard.html')

def restaurant(request, id):
    return render(request, 'restaurants/pages/restaurants-view.html', context={
        'restaurant': get_object_or_404(Restaurant, id=id),
     })

def home(request):
    restaurants = Restaurant.objects.all().order_by('-id')

    return render(request, 'restaurants/pages/home.html', context={
        'restaurants': restaurants,  
    })

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurants/pages/add.html'
    success_url = reverse_lazy('restaurants:home')
    
    def form_valid(self, form):
        print("Form is valid")
        form.save()
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return self.success_url