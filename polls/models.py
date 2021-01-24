from django.core.exceptions import RequestDataTooBig
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    class Meta:
        abstract = True

class ChoiceNumber(Choice):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_number = models.IntegerField()
    votes = models.IntegerField(default=0)

class ChoiceText(Choice):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)