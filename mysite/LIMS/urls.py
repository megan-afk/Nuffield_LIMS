from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = "LIMS"

urlpatterns = [
    path("", views.IndexView, name="index"),

    path('sample/<int:sample_id>', views.DetailView, name="sample"),
    path('extraction/<int:extraction_id>', views.ExtractionView, name="extraction"),
    path('auto_complete', views.auto_complete, name="auto_complete"),

]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
