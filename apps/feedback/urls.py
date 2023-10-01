from django.urls import path
from .views import FeedbackCreateAPIView, FeedbackListAPIView

urlpatterns = [
    path("create/", FeedbackCreateAPIView.as_view(), name="create-feedback"),
    path("list/", FeedbackListAPIView.as_view(), name="list-feedback"),
]
