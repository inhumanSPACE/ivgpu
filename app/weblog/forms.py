from django.forms import ModelForm

from weblog.models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleUpdateForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "content"]
