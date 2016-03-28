from django.contrib.auth.models import User
from rest_framework import serializers
from duckapp.models import Question, UserProfile, Answer, Tag
# from rest_framework.authtoken.models import Token


class QuestionSerializer(serializers.ModelSerializer):
    asker = serializers.ReadOnlyField(source='asker.id')

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

    def create(self, validated_data):
        new_user = User.objects.create(username=validated_data['username'])
        new_user.set_password(validated_data['password'])
        new_user.save()
        UserProfile.objects.create(user=new_user)
        return new_user
