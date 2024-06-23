from django.shortcuts import redirect, render, get_object_or_404
from .models import Job
from .forms import JobForm

def jobs(request):
    jobs = Job.objects.all()
    return render (request, 'jobs/index.html', {'jobs' : jobs})


def job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render (request, 'jobs/job.html', {'job' : job})


def create(request):
    if request.method == 'POST':
        form = JobForm(request.POST,  request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('get_jobs')
    else:
        form = JobForm()
    
    return render(request, 'jobs/create.html', {'form' : form})


