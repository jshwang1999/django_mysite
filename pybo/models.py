from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# DB 모델들


class Notices(models.Model):
    objects = models.Manager()
    n_title = models.CharField(max_length=100)
    n_body = models.TextField()
    n_hit = models.PositiveIntegerField(default=0)
    n_input_date = models.DateTimeField('date published', default=timezone.now())


class Question(models.Model):  # 질문글
    # create table Question(subject char(200), content varchar, create_date date
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    attachment = models.ImageField(upload_to="media", null=True, blank=True)


class Answer(models.Model):  # 답변글
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


def __str___(self):
    return self.subject
