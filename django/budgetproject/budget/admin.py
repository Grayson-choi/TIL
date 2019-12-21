from django.contrib import admin
from .models import Project, Expenses, Category

admin.site.register(Project)
admin.site.register(Expenses)
admin.site.register(Category)

# Register your models here.
