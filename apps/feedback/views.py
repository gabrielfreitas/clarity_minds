from datetime import datetime
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, ListView
from .models import Feedback
from apps.core.models import SchoolClass, Student, Teacher


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ["student", "emoji", "message", "is_anonymous"]
    # success_url = reverse_lazy("thank-you")
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        student_email = request.POST.get("email")
        try:
            student = Student.objects.get(email=student_email)
        except Student.DoesNotExist:
            school_class = SchoolClass.objects.filter(name__icontains="Teste").first()
            student = Student.objects.create(
                name="Teste",
                email=student_email,
                school_class=school_class,
            )
            # return render(
            #     request,
            #     "feedback-error.html",
            #     {"message": "Aluno não encontrado!"},
            # )

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
        is_anonymous = True if request.POST.get("is_anonymous") else False
        feedback = Feedback.objects.create(
            student=student,
            emoji=request.POST.get("emoji"),
            message=request.POST.get("message"),
            is_anonymous=is_anonymous,
        )
        return HttpResponseRedirect(reverse_lazy("thank-you"))


class SchoolClassListView(ListView):
    model = SchoolClass
    template_name = "school_classes.html"
    start_date = None

    def get_queryset(self):
        start_date_param = self.request.GET.get("start_date")
        if start_date_param:
            self.start_date = datetime.strptime(start_date_param, "%Y-%m-%d")
        else:
            self.start_date = datetime.now().date()
        try:
            teacher = Teacher.objects.get(user=self.request.user)
        except Teacher.DoesNotExist:
            return render(
                self.request,
                "feedback-error.html",
                {"message": "Professor não encontrado!"},
            )
        return teacher.classes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["start_date"] = self.start_date
        return context


class FeedbackListView(ListView):
    model = Feedback
    template_name = "feedbacks.html"
    start_date = None

    def get_queryset(self):
        start_date_param = self.request.GET.get("start_date")
        if start_date_param:
            self.start_date = datetime.strptime(start_date_param, "%Y-%m-%d")
        else:
            self.start_date = datetime.now().date()
        try:
            teacher = Teacher.objects.get(user=self.request.user)
        except Teacher.DoesNotExist:
            return render(
                self.request,
                "feedback-error.html",
                {"message": "Professor não encontrado!"},
            )
        return (
            Feedback.objects.filter(
                student__school_class=self.kwargs["pk"],
                created_at__date=self.start_date,
            )
            .annotate(total=Count("emoji"))
            .order_by("-total")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["start_date"] = self.start_date
        context["school_class"] = SchoolClass.objects.get(id=self.kwargs["pk"])
        return context
