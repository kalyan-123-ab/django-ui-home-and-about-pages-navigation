# from django.contrib import admin
# from .models import projectapp

# admin.site.register(projectapp)

# projectapp/admin.py
from django.contrib import admin
from .models import projectapp

class projectappModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','about')  

admin.site.register(projectapp, projectappModelAdmin)
