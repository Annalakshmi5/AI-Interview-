from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('hr/dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('candidate/dashboard/', views.candidate_dashboard, name='candidate_dashboard'),

    # Interview management
    path('interviews/create/', views.create_interview, name='create_interview'),
   
    # HR Question Management
    

    # Add these for editing/deleting questions
    path('hr/assign-job/', views.assign_job, name='assign_job'),
    path('job/register/<int:job_id>/', views.job_register, name='job_register'),
     path('interviews/edit/<int:id>/', views.edit_interview, name='edit_interview'),
    path('interviews/delete/<int:id>/', views.delete_interview, name='delete_interview'),
]
    
