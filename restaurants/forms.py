from django import forms
from .models import Restaurant, Country, City, Neighborhood, Category, State
from utils.form_widget import MultipleSelect2Widget, Select2Widget

class RestaurantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        
        self.fields['title'] = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['country'] = forms.ModelChoiceField(
            queryset=Country.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['state'] = forms.ModelChoiceField(
            queryset=State.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['city'] = forms.ModelChoiceField(
            queryset=City.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['neighborhood'] = forms.ModelChoiceField(
            queryset=Neighborhood.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['description'] = forms.CharField(
            widget=forms.Textarea(attrs={'class': 'form-control'}),
            required=True
        )
        self.fields['opening_hours'] = forms.TimeField(
            widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            required=True
        )
        self.fields['closing_hours'] = forms.TimeField(
            widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            required=True
        )
        self.fields['img_restaurant'] = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            required=False
        )
        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True
        )
        
        if 'instance' in kwargs and kwargs['instance']:
            instance = kwargs['instance']
            if instance.country:
                self.fields['state'].queryset = State.objects.filter(country=instance.country)
            if instance.state:
                self.fields['city'].queryset = City.objects.filter(state=instance.state)
            if instance.city:
                self.fields['neighborhood'].queryset = Neighborhood.objects.filter(city=instance.city)
        
    class Meta:
        model = Restaurant
        fields = '__all__'