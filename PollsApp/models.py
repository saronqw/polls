from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now, editable=False)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Vote(models.Model):
    text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        if self.text is None:
            return 'User: ' + str(self.user) + ', question: ' + str(self.question) + ', choice: ' + str(self.choice)
        return 'User: ' + str(self.user) + ', question: ' + str(self.question) + ', text: ' + str(self.text)
