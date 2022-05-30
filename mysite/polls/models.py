import datetime

from django.db import models
from django.utils import timezone

class Exam(models.Model):
    title  = models.CharField(max_length=200)
    q_num = models.IntegerField(default=0) # 문제 개수
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model): # 학생 or 정답(num : 1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    num = models.IntegerField(default=0) # 학번
    choice_text = models.CharField(max_length=200)
    correct =  models.CharField(max_length=10)
    def __str__(self):
        return self.choice_text