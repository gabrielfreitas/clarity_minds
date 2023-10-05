from datetime import datetime, timedelta
from django.db.models import Count
from django.utils import timezone
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Feedback
from .serializers import FeedbackSerializer
from apps.core.models import Student


class FeedbackCreateAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        emoji = request.data.get("emoji")
        message = request.data.get("message")

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return Response(
                {"error": "Aluno não cadastrado"}, status=status.HTTP_400_BAD_REQUEST
            )

        data = {"student": student.id, "emoji": emoji, "message": message}

        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackListAPIView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        start_date_param = self.request.query_params.get("start_date")
        if start_date_param:
            start_date = datetime.strptime(start_date_param, "%Y-%m-%d")
        return Feedback.objects.filter(
            student__school_class__teachers=self.request.user,
            created_at__date=start_date,
        )
