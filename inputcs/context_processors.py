from django.db.models import Count
from . import models
import datetime


def base_context(request):
    defects = models.Sheet.objects.all().order_by('-id')[:10]
    # coord = models.AjaxImage.objects.all()
    side = models.Sheet.objects.all()[:1]
    today = datetime.datetime.today().date()
    number_defects_day = models.Sheet.objects.filter(created__date=today).count()

    return {
        'defects': defects,
        # 'coord' : coord,
        'side' : side,
        'number_defects_day' : number_defects_day
    }

