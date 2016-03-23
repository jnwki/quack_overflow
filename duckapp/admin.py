from django.contrib import admin
from duckapp.models import Tag, Answer, Question, UserProfile


admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(UserProfile)
