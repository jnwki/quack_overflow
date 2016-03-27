from django.conf.urls import url
from django.contrib import admin
from duckapp.views import IndexView, UserCreateView, QuestionCreateView, AnswerCreateView, UpvoteView, \
    DownvoteView, UserDetailView, QuestionListCreateAPIView, QuestionRetrieveUpdateDestroyAPIView, \
    UserCreateAPIView
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^signup/', UserCreateView.as_view(), name='signup'),
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout_then_login, name='logout'),
    url(r'^question/createquestion/', QuestionCreateView.as_view(), name='question_create'),
    url(r'^question/(?P<pk>\d+)/createanswer/', AnswerCreateView.as_view(), name='answer_create'),
    url(r'^upvote/(?P<pk>\d+)', UpvoteView.as_view(), name='upvote'),
    url(r'^downvote/(?P<pk>\d+)', DownvoteView.as_view(), name='downvote'),
    url(r'^userdetail/(?P<pk>\d+)', UserDetailView.as_view(), name='user_detail'),
    url(r'^api/questions/listcreate/', QuestionListCreateAPIView.as_view(), name='api_question_list_create'),
    url(r'^api/question/(?P<pk>\d+)', QuestionRetrieveUpdateDestroyAPIView.as_view(), name='api_question_retrieve_update_destroy'),
    url(r'^api/usercreate/', UserCreateAPIView.as_view(), name='api_user_create'),
    url(r'^api_token_auth/', views.obtain_auth_token)
]
