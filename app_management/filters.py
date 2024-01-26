import django_filters
from django import forms
from .models import Shops

class ShopsFilter(django_filters.FilterSet):
    region = django_filters.CharFilter(lookup_expr='iexact', widget=forms.Select(attrs={'class': 'form-control'}))
    store_type = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Shops
        fields = ['region', 'store_type']
