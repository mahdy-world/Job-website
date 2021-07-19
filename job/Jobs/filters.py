import django_filters

from .models import *
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    discrpations = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = ['title' , 'job_type' , 'discrpations' , 'salary' , 'experience' , 'category']
        