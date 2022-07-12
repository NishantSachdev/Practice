from django.contrib import admin
from .models import employee
from .models import department

admin.site.register(employee)
admin.site.register(department)