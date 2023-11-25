from django.db import models

# Create your models here.
from django.db import models


# DB 모델들
class Question(models.Model):
    # create table Question(subject char(200), content varchar, create_date date
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()