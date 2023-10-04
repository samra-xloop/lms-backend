from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Unit)
admin.site.register(Course)