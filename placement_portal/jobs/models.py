from django.db import models
from accounts.models import User

class Job(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.TextField() 
    deadline = models.DateField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure the company (User) is a recruiter
        if self.company.role != 'recruiter':
            raise ValueError("The user must have 'recruiter' role to post a job.")
        super().save(*args, **kwargs)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('applied', 'Applied'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure the student (User) is a student
        if self.student.role != 'student':
            raise ValueError("The user must have 'student' role to apply for a job.")
        super().save(*args, **kwargs)
