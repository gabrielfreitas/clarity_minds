from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .models import Feedback
from apps.core.models import Student


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ["student", "emoji", "message"]
    success_url = reverse_lazy("thank-you")
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        student_email = request.POST.get("email")
        try:
            student = Student.objects.get(email=student_email)
        except Student.DoesNotExist:
            return render(
                request,
                "feedback-error.html",
                {"message": "Aluno não encontrado!"},
            )

        feedback = Feedback.objects.filter(
            student=student,
            created_at__date=datetime.now().date(),
        )
        if feedback:
            return render(
                request,
                "feedback-error.html",
                {"message": "Você já enviou um feedback hoje!"},
            )
        feedback = Feedback.objects.create(
            student=student,
            emoji=request.POST.get("emoji"),
            message=request.POST.get("message"),
        )
        return HttpResponseRedirect(self.get_success_url())


# class FeedbackListAPIView(generics.ListAPIView):
#     serializer_class = FeedbackSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         start_date_param = self.request.query_params.get("start_date")
#         if start_date_param:
#             start_date = datetime.strptime(start_date_param, "%Y-%m-%d")
#         return Feedback.objects.filter(
#             student__school_class__teachers=self.request.user,
#             created_at__date=start_date,
#         )
