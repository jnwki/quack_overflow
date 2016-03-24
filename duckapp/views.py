from django.views.generic import CreateView, ListView, View, DetailView
from django.contrib.auth.models import User
from duckapp.models import UserProfile, Question, Answer
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from serializers import QuestionSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from duckapp.permissions import IsOwnerOrReadOnly


class IndexView(ListView):
    template_name = 'index.html'
    model = Question


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        user_object = form.save()
        profile = UserProfile.objects.create(user=user_object)
        profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'question_text', 'tags']

    def form_valid(self, form):
        new_question = form.save(commit=False)
        new_question.asker = self.request.user
        new_question.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['title', 'answer_text']

    def form_valid(self, form, **kwargs):
        answer_form = form.save(commit=False)
        answer_form.question = Question.objects.get(pk=self.kwargs['pk'])
        answer_form.answerer = self.request.user
        answer_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class UpvoteView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user:
            answer = Answer.objects.get(pk=self.kwargs['pk'])
            upvoter = UserProfile.objects.get(user=self.request.user)

            if answer in upvoter.upvotes.all():
                print("user has already upvoted that answer")
                return HttpResponseRedirect(reverse('index'))
            elif answer in upvoter.downvotes.all():
                print("user has already downvoted that answer")
                return HttpResponseRedirect(reverse('index'))
            elif answer.answerer == self.request.user:
                print("You cannot vote on your own posts")
                return HttpResponseRedirect(reverse('index'))

            upvoter.upvotes.add(answer)
            upvoter.save()

            question_answerer = UserProfile.objects.get(user=answer.answerer)
            question_answerer.score += 10
            question_answerer.save()

            answer.score += 1
            answer.save()

            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponseRedirect(reverse('login'))


class DownvoteView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user:
            answer = Answer.objects.get(pk=self.kwargs['pk'])
            downvoter = UserProfile.objects.get(user=self.request.user)

            if answer in downvoter.downvotes.all():
                print("user has already downvoted that answer")
                return HttpResponseRedirect(reverse('index'))
            elif answer in downvoter.upvotes.all():
                print("user has already upvoted that answer")
                return HttpResponseRedirect(reverse('index'))
            elif answer.answerer == self.request.user:
                print("You cannot vote on your own posts")
                return HttpResponseRedirect(reverse('index'))

            downvoter.downvotes.add(answer)
            downvoter.score -= 1
            downvoter.save()

            question_answerer = UserProfile.objects.get(user=answer.answerer)
            question_answerer.score -= 5
            question_answerer.save()

            answer.score -= 1
            answer.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            return HttpResponseRedirect(reverse('login'))


class UserDetailView(DetailView):
    model = UserProfile


class QuestionListCreateAPIView(ListCreateAPIView):
        serializer_class = QuestionSerializer
        queryset = Question.objects.all()
        permission_classes = (IsAuthenticatedOrReadOnly,)


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Question.objects.all()


# should probably be just a createview. needs to attach a userprofile
class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# don't think I need this view as userprofile (not user) would be what others would want to see
class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = User.objects.all()
