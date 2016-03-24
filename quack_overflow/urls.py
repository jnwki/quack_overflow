from django.conf.urls import url
from django.contrib import admin
from duckapp.views import IndexView, UserCreateView, QuestionCreateView, AnswerCreateView, UpvoteView, DownvoteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^signup/', UserCreateView.as_view(), name='signup'),
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout_then_login, name='logout'),
    url(r'^question/createquestion/', QuestionCreateView.as_view(), name='question_create'),
    url(r'^question/(?P<pk>\d+)/createanswer/', AnswerCreateView.as_view(), name='answer_create'),
    url(r'^upvote/(?P<pk>\d+)', UpvoteView.as_view(), name='upvote'),
    url(r'^downvote/(?P<pk>\d+)', DownvoteView.as_view(), name='downvote')

]
