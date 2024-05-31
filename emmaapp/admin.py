from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'matric_number', 'cgpa')
    search_fields = ('first_name', 'last_name', 'email', 'matric_number')
    list_filter = ('cgpa',)
    ordering = ('last_name', 'first_name')

admin.site.register(Candidate, CandidateAdmin)
