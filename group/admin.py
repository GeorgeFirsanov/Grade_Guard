from django.contrib import admin
#from .models import Group
from . import models as m
# Register your models here.
admin.site.register(m.Group)
admin.site.register(m.Student)
admin.site.register(m.Subject)
