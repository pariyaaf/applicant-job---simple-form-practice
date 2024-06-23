from django.db import models
from jobs.models import Job
from django.contrib.auth.models import User

class Applicant(models.Model):
    resume = models.FileField(upload_to='resumes/')
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    application_jobs  = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"