from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from weblog.views import (ArticleAPICreate, ArticleAPIDelete, ArticleAPIList,
                          ArticleAPIUpdate, ArticleCreate, ArticleDelete,
                          ArticleList, ArticleUpdate, ProfileCreate,
                          ProfileLogin, logout_profile)

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/article/", ArticleList.as_view(), name="home"),
    path("api/v1/article/create/", ArticleCreate.as_view(), name="create"),
    # path("api/v1/auth/", include("rest_framework.urls")),
    # path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/signup/", ProfileCreate.as_view(), name="signup"),
    path("api/v1/login/", ProfileLogin.as_view(), name="login"),
    path("api/v1/logout/", logout_profile, name="logout"),
    # path("api/v1/article/", ArticleAPIList.as_view()),
    # path("api/v1/article/<int:pk>/", ArticleAPIList.as_view()),
    # path("api/v1/article/post/", ArticleAPICreate.as_view()),
    path("api/v1/article/update/<int:pk>/", ArticleUpdate.as_view(), name="update"),
    path("api/v1/article/delete/<int:pk>/", ArticleDelete.as_view(), name="delete"),
]
