from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company']  # فیلدهایی که در فرم استفاده می‌شوند باید با مدل مطابقت داشته باشند
