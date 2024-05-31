from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .models import Candidate
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CandidateSerializer

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

def candidate_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        matric_number = request.POST.get('matric_number')
        cgpa = request.POST.get('cgpa')
        resume = request.FILES.get('resume')
        result = request.FILES.get('result')
        essay1 = request.FILES.get('essay1')
        essay2 = request.FILES.get('essay2')
        essay3 = request.FILES.get('essay3')

        candidate = Candidate(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            matric_number=matric_number,
            cgpa=cgpa,
            resume=resume,
            result=result,
            essay1=essay1,
            essay2=essay2,
            essay3=essay3
        )
        candidate.save()

         # Send email to admin
        email_subject = 'New Candidate Submission'
        email_body = f'''
        A new candidate has submitted their details:

        First Name: {first_name}
        Last Name: {last_name}
        Phone Number: {phone_number}
        Email: {email}
        Matric Number: {matric_number}
        CGPA: {cgpa}
        '''

        email_message = EmailMessage(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            ['dj005571@gmail.com']  # Replace with the admin's email address
        )

        # Attach files to the email
        if resume:
            email_message.attach(resume.name, resume.read(), resume.content_type)
        if result:
            email_message.attach(result.name, result.read(), result.content_type)
        if essay1:
            email_message.attach(essay1.name, essay1.read(), essay1.content_type)
        if essay2:
            email_message.attach(essay2.name, essay2.read(), essay2.content_type)
        if essay3:
            email_message.attach(essay3.name, essay3.read(), essay3.content_type)

        email_message.send()

        return redirect(reverse('candidate_list'))
    return render(request, 'candidate_form.html')

def candidate_update(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.phone_number = request.POST.get('phone_number')
        candidate.email = request.POST.get('email')
        candidate.matric_number = request.POST.get('matric_number')
        candidate.cgpa = request.POST.get('cgpa')

        if 'resume' in request.FILES:
            candidate.resume = request.FILES['resume']
        if 'result' in request.FILES:
            candidate.result = request.FILES['result']
        if 'essay1' in request.FILES:
            candidate.essay1 = request.FILES['essay1']
        if 'essay2' in request.FILES:
            candidate.essay2 = request.FILES['essay2']
        if 'essay3' in request.FILES:
            candidate.essay3 = request.FILES['essay3']

        candidate.save()
        return redirect(reverse('candidate_detail', args=[candidate.id]))
    return render(request, 'candidate_form.html', {'candidate': candidate})

def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        candidate.delete()
        return redirect(reverse('candidate_list'))
    return render(request, 'candidate_confirm_delete.html', {'candidate': candidate})

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    parser_classes = (MultiPartParser, FormParser)
