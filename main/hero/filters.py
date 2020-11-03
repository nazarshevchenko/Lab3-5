import django_filters
from django_filters import CharFilter
from .models import *
from django.forms import TextInput

class SearchFilter(django_filters.FilterSet):
    note = CharFilter(field_name='text', lookup_expr='icontains',)

    class Meta:
        model = Plane
        fields = []
