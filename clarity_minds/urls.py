"""
URL configuration for clarity_minds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from apps.feedback.views import (
    FeedbackCreateView,
    FeedbackListView,
    SchoolClassListView,
)

urlpatterns = [
    path("", FeedbackCreateView.as_view(), name="home"),
    path("schools-classes/", SchoolClassListView.as_view(), name="schools-classes"),
    path("feedbacks/<int:pk>/", FeedbackListView.as_view(), name="feedback-detail"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("apps.users.urls")),
    path("api/", include("apps.feedback.urls")),
    # path("login/", views.login), # é utilizado o do modulo users
    path(
        "thank-you/",
        TemplateView.as_view(template_name="thank-you.html"),
        name="thank-you",
    ),
]
