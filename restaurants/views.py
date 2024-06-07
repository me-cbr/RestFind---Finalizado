import os
from django.http import JsonResponse

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from utils.pagination import make_pagination

from .models import *
from .forms import RestaurantForm

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

def dashboard(request):
    return render(request, 'restaurants/pages/dashboard.html')

def restaurant(request, id):
    return render(request, 'restaurants/pages/restaurants-view.html', context={
        'is_detail_page': True,
        'restaurant': get_object_or_404(Restaurant, id=id),
     })

def home(request):
    restaurants = Restaurant.objects.all().order_by('-id')

    page, pagination = make_pagination(request, restaurants, PER_PAGE)

    return render(request, 'restaurants/pages/home.html', context={
        'restaurants': page,  
        'pagination': pagination,
    })

def category(request, category_id):
    restaurants = Restaurant.objects.filter(
        category_id=category_id
    ).order_by('-id')

    page, pagination = make_pagination(request, restaurants, PER_PAGE)

    return render(request, 'restaurants/pages/home.html', context={
        'restaurants': page, 
        'pagination': pagination,
        'title': f'{restaurants[0].category.name} - Category | '
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    restaurant = Restaurant.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
    ).order_by('-id')

    page, pagination = make_pagination(request, restaurant, PER_PAGE)

    return render(request, 'restaurants/pages/../base_templates/global/partials/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'restaurant': page,
        'pagination': pagination,
        'additional_url_query': f'&q={search_term}',
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