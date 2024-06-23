from django.shortcuts import render, redirect, get_object_or_404
from .models import Applicant
from .forms import ApplicantForm



def applicant(request, user_id):
    applicants = Applicant.objects.filter(user__id=user_id).all()
    return render(request, "applicants/applicant.html", {'applicants': applicants})


def create(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            return redirect('get_jobs') 
    else:
        form = ApplicantForm()
    
    return render(request, 'applicants/create.html', {'form': form})


