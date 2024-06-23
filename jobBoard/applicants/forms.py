from django import forms
from .models import Applicant
from jobs.models import Job

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['user', 'application_jobs', 'resume'] 