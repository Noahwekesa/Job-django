import django_filters
from .models import Job, ApplyJob
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ('title', 'city', 'job_type', 'industry',)

class ExpFilter(django_filters.FilterSet):
    # experience = django_filters.NumberFilter(lookup_expr='icontains')
    minExperience = django_filters.NumberFilter(field_name='experience', lookup_expr='gte', label='Min Experience')
    maxExperience = django_filters.NumberFilter(field_name='experience', lookup_expr='lte', label='Max Experience')
    class Meta:
        model = ApplyJob
        fields = ('experience',)