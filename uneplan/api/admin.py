from django.contrib import admin

from .models import Department
class Computers(admin.ModelAdmin):
    model=Department

admin.site.register(Department)

# Register your models here.
