from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from weblog.forms import ArticleCreateForm, ArticleUpdateForm
from weblog.models import Article
from weblog.serializers import (ArticleCreateSerializer, ArticleSerializer,
                                ArticleUpdateSerializer)


class ArticleAPIList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class ArticleAPICreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer


class ArticleAPIDelete(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleList(ListView):
    model = Article
    template_name = "weblog/index.html"
    context_object_name = "articles"


class ArticleCreate(CreateView):
    form_class = ArticleCreateForm
    template_name = "weblog/article.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление статьи"
        return context


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = "weblog/article_update.html"
    success_url = reverse_lazy("home")
    # fields = ["name", "content"]

    # def get_queryset(self):
    #     return Article.objects.filter(name=self.request.name)


class ArticleDelete(DeleteView):
    model = Article
    template_name = "weblog/index.html"
    success_url = reverse_lazy("home")


class ProfileCreate(CreateView):
    form_class = UserCreationForm
    template_name = "weblog/signup.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        profile = form.save()
        login(self.request, profile)
        return redirect("home")


class ProfileLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "weblog/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy("home")


def logout_profile(request):
    logout(request)
    return redirect("login")
