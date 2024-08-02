from django.contrib import admin
from .models import Sample, Extraction, QC, Sequencing
# Register your models here.
admin.site.register(Extraction)
admin.site.register(Sample)
admin.site.register(QC)
admin.site.register(Sequencing)
