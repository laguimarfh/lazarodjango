from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from . import models
from inputcs.models import Sheet
from inputcs.forms import SheetForm
from django.db.models import Q
import datetime

# Create your views here.
class HomeView(ListView):
    """
    The CS homepage
    """
    template_name = 'inputcs/home.html'
    model: Sheet
    context_object_name = 'defects'
    

    def get_queryset(self):
        return Sheet.objects.all().order_by('-created')

        
class DefectCreateView(CreateView):
    form_class = SheetForm
    template_name = 'inputcs/input.html'
    
    def get_context_data(self, **kwargs):
        sheet_form = SheetForm
        context = super().get_context_data(**kwargs)
        context['sheet_form'] = sheet_form
        
        return context

class DefectDetailView(DetailView):
    """
    The CS homepage
    """
    model = Sheet
    template_name = 'inputcs/defects_detail.html'
    context_object_name = 'defect'

def is_valid_queryparam(param):
    return param != '' and param is not None


def bootstrapfilter(request):
    qs = models.Sheet.objects.all()
    categories = models.Sheet.objects.all()
    process_contains_query = request.GET.get('process_contains')
    location_contains_query = request.GET.get('location_contains')
    defect_contains_query = request.GET.get('defect_contains')
    id_exact_query = request.GET.get('id_exact')
    process_or_defect_query = request.GET.get('process_or_defect')
    # view_count_min = request.GET.get('view_count_min')
    # view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    location_list = request.GET.get('location')
    # reviewed = request.GET.get('reviewed')
    # not_Reviewed = request.GET.get('notReviewed')
    print(
        process_contains_query,
        id_exact_query,
        process_or_defect_query,
        date_max,
        date_min,
        location_list,
        location_contains_query,
        defect_contains_query,
        
        )

    if is_valid_queryparam(process_contains_query):
        qs = qs.filter(process__icontains=process_contains_query)
    
    if is_valid_queryparam(location_contains_query):
        qs = qs.filter(location__icontains=location_contains_query)
    
    if is_valid_queryparam(defect_contains_query):
        qs = qs.filter(defect__icontains=defect_contains_query)

    if is_valid_queryparam(id_exact_query):
        qs = qs.filter(id__exact=id_exact_query)

    elif is_valid_queryparam(process_or_defect_query):
        qs = qs.filter(Q(process__icontains=process_or_defect_query)
                       | Q(author__name__icontains=process_or_defect_query)
                       ).distinct()

    # if is_valid_queryparam(view_count_min):
    #     qs = qs.filter(views__gte=view_count_min)

    # if is_valid_queryparam(view_count_max):
    #     qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(created__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(created__lt=date_max)

    if is_valid_queryparam(location_list) and location_list != 'Choose...':
        qs = qs.filter(location=location_list)

    # if reviewed == 'on':
    #     qs = qs.filter(reviewed=True)
    # elif not_Reviewed == 'on':
    #     qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        
    }
    return render(request, "inputcs/bootstrap_form.html", context)
