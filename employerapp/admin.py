from atexit import register
from django.contrib import admin

from employerapp.models import EmployerRegModel

# Register your models here.
admin.site.register(EmployerRegModel)