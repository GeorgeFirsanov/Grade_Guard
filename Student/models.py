from django.db import models

from group.models import Student

def extends(klass):
    def decorator(func):
        setattr(klass, func.__name__, func)
        return func
    return decorator