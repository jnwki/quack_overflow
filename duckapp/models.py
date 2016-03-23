from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    score = models.IntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Question(models.Model):
    asker = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    question_text = models.TextField()
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    answerer = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question)
    answer_text = models.TextField()
    score = models.IntegerField()
