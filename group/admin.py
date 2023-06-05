from django.contrib import admin
#from .models import Group
from . import models as m
# Register your models here.
admin.site.register(m.Group)
admin.site.register(m.Student)
admin.site.register(m.Subject)
<<<<<<< HEAD
admin.site.register(m.Atom)
admin.site.register(m.Category)
=======
>>>>>>> c05ce29b28c2fc84802b8cf8931a9d892b8fe274
admin.site.register(m.Professor)