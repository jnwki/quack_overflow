# from django.shortcuts import render
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.models import User
from duckapp.models import UserProfile, Question, Answer
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


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
            answer.score += 1
            answerer_var = UserProfile.objects.get(user=answer.answerer)
            answerer_var.score += 10
            answerer_var.save()
            answer.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login'))


class DownvoteView(View):
    pass
