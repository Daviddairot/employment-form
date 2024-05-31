from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'matric_number', 'cgpa', 'resume', 'result', 'essay1', 'essay2', 'essay3']
