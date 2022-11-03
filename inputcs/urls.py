from django.urls import path

from . import views
from .views import bootstrapfilter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('defect/<int:pk>', views.DefectDetailView.as_view(), name='defect-detail'),
    path('input/', views.DefectCreateView.as_view(), name='input'),  # Set root to home view
    # path('list/', views.sheet_list, name="sheet-list"),
    path('filter/', bootstrapfilter, name='bootstrap')
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)