import django_filters
from . import models

class SheetFilter(django_filters.FilterSet):
    class Meta:
        model = models.Sheet
        fields = ['id','process', 'defect','side','location','created']
