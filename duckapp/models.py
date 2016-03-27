from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Question(models.Model):
    asker = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    question_text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return "{}".format(self.title)


class Answer(models.Model):
    answerer = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question)
    answer_text = models.TextField()
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score", "-timestamp"]

    def __str__(self):
        return "{}".format(self.title)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    score = models.IntegerField(default=0)
    sign_up_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(Answer, related_name='upvote')
    downvotes = models.ManyToManyField(Answer, related_name='downvote')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Question)
def make_question_reward(sender, instance=None, created=False, **kwargs):
    if created:
        instance.asker.userprofile.score += 5
        instance.asker.userprofile.save()
