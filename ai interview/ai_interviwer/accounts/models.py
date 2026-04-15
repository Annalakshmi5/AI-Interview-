from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('hr', 'HR'),
        ('candidate', 'Candidate'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class Candidate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    linkedin_url = models.URLField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Interview(models.Model):
    hr = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hr_interviews',
        limit_choices_to={'user_type': 'hr'}
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='candidate_interviews'
    )
    position = models.CharField(max_length=200)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    duration_minutes = models.IntegerField(default=60)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.position} - {self.candidate.user.username} ({self.date:%Y-%m-%d %H:%M})"
