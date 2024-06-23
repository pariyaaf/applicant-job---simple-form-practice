from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs, name= 'get_jobs'),
    path('<int:job_id>/', views.job, name= 'get_job'),
    path('create/', views.create, name= 'create_job'),

]