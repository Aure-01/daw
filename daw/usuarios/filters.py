import django_filters
from django_filters import DateFilter, CharFilter
from usuarios.models import *
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter (field_name="date_created, lookup_expr'lte')
    note = CharFilter (field_name='note', lookup_expr= 'incontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['custome', 'date_created']
