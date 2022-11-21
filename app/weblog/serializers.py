from rest_framework import serializers

from weblog.models import Article

# class CreateProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ""


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["name", "content"]
