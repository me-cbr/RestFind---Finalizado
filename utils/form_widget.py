from django.forms import widgets
from django import forms
class Select2Widget(forms.Select):
    def __init__(self, attrs={}, choices=()):
        attrs['class'] = 'enable-select2'
        super(Select2Widget, self).__init__(attrs, choices)


class MultipleSelect2Widget(forms.SelectMultiple):
    def __init__(self, attrs={}, choices=()):
        attrs['class'] = 'enable-select2'
        super(MultipleSelect2Widget, self).__init__(attrs, choices)