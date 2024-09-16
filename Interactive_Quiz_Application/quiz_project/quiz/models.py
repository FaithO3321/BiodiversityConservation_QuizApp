from django.db import models
from django.contrib.auth.models import User
import uuid

class Question(models.Model):
    text = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    shareable_id = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return f'{self.user.username} - {self.score}'
