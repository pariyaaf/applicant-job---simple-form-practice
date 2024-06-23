from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.applicant, name='get_applicants'),
    path('create/', views.create, name= 'create_applicant'),

]