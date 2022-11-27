from rest_framework import serializers
from djoser.serializers import UserCreateSerializer  # djoser serializers
from django.contrib.auth import get_user_model  # djoser serializers
from blog_app.models import BlogPost, Feedback

User = get_user_model()


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
        lookup_field = "slug"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ["date_received"]


class DataSerializer(serializers.Serializer):
    xcors = serializers.ListField(max_length=300)
    ycors = serializers.ListField(max_length=300)
    created = serializers.DateTimeField()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = {"id", "email", "name", "password"}
