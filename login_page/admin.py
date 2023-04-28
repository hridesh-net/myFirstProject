from django.contrib import admin
from .models import Candidates

# Register your models here.

# admin.site.register(Candidates)

@admin.register(Candidates)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date']
    ordering = ('name',)