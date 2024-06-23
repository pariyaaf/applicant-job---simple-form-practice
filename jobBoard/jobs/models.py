from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
