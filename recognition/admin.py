from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Batch, Student

admin.site.register(Batch)
admin.site.register(Student)