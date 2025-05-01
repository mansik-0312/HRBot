from django.db import models

# Create your models here.

class CandidateResponse(models.Model):
    session_id = models.CharField(max_length=300) #track conversation
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session_id} - {self.question}"

class InterviewResponse(models.Model):
    session_id = models.CharField(max_length=100)
    user_message = models.TextField()
    response = models.TextField()
    conversation_end = models.BooleanField(default=False)

    def __str__(self):
        return f"Session: {self.session_id} - User: {self.user_message[:50]}.... "