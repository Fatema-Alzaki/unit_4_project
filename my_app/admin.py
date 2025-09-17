from django.contrib import admin
from .models import Material, PrintJob, Printer, PrintHistory  # import your models

# Register the models so they show up in the Django Admin
admin.site.register(Material)
admin.site.register(PrintJob)
admin.site.register(Printer)
admin.site.register(PrintHistory)
