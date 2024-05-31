from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'matric_number', 'cgpa', 'resume', 'result', 'essay1', 'essay2', 'essay3']
