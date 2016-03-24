from django.contrib.auth.models import User
from rest_framework import serializers
from duckapp.models import Question, UserProfile, Answer, Tag


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
