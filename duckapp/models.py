from django.db import models


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

    def __str__(self):
        return "{}".format(self.title)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    score = models.IntegerField(default=0)
    sign_up_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(Answer, related_name='upvote')
    downvotes = models.ManyToManyField(Answer, related_name='downvote')
