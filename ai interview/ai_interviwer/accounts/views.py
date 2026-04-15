from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from .forms import SignUpForm, LoginForm, InterviewForm, QuestionForm, AssignJobForm, JobRegistrationForm
from .models import Interview, User, Question, JobRegistration, Candidate


# --------------------
# AUTHENTICATION
# --------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! Please log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'hr':
                    return redirect('hr_dashboard')
                else:
                    return redirect('candidate_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


# --------------------
# DASHBOARDS
# --------------------
@login_required
def hr_dashboard(request):
    interviews = Interview.objects.all()
    return render(request, 'accounts/hr_dashboard.html', {'interviews': interviews})


@login_required
def create_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')
    else:
        form = InterviewForm()
    return render(request, 'interview_form.html', {'form': form})


@login_required
def edit_interview(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')
    else:
        form = InterviewForm(instance=interview)
    return render(request, 'interview_form.html', {'form': form})


@login_required
def delete_interview(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    if request.method == 'POST':
        interview.delete()
        return redirect('hr_dashboard')
    return render(request, 'confirm_delete.html', {'object': interview})