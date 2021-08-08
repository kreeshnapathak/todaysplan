from myapp.models import Plan
from django.contrib import admin

# Register your models here.

@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
    list_display=["id",'item']
