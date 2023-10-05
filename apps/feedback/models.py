from django.db import models

from apps.core.models import DefaultModel

EMOJI_CHOICES = (
    ("😃", "😃 - Feliz"),
    ("😊", "😊 - Legal"),
    ("😐", "😐 - Normal/Neutro"),
    ("😥", "😥 - Preocupado"),
    ("😞", "😞 - Chateado"),
    ("😫", "😫 - Triste"),
    ("😵", "😵 - Cansado"),
    ("😡", "😡 - Raiva"),
)

class Feedback(DefaultModel):
    student = models.ForeignKey(
        "core.Student",
        on_delete=models.CASCADE,
        related_name="feedbacks",
        verbose_name="Aluno",
    )
    emoji = models.CharField("Emoji", choices=EMOJI_CHOICES, max_length=255)
    message = models.TextField("Mensagem")

    def __str__(self):
        return f"{self.student.name} em {self.created_at.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ["-created_at"]
