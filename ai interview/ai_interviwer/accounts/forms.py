from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Interview

# ------------------------
# User Signup Form
# ------------------------
class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


# ------------------------
# Login Form
# ------------------------
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# ------------------------
# Interview Creation Form (HR schedules interviews)
# ------------------------
class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['hr', 'candidate', 'position', 'date', 'notes', 'duration_minutes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


# ------------------------
# HR - Question Posting Form
# ------------------------


