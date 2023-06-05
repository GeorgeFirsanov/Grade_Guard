from django.contrib import admin
#from .models import Group
from . import models as m
# Register your models here.
admin.site.register(m.Group)
admin.site.register(m.Student)
admin.site.register(m.Subject)
admin.site.register(m.Atom)
admin.site.register(m.Category)
admin.site.register(m.Professor)