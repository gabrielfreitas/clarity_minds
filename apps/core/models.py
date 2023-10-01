import uuid
from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_updated_by",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = "created_at"


# class Discipline(DefaultModel):
#     name = models.CharField("Nome", max_length=255)

#     class Meta:
#         verbose_name = "Disciplina"
#         verbose_name_plural = "Disciplinas"
#         ordering = ["name"]


class Teacher(DefaultModel):
    name = models.CharField("Nome", max_length=255)
    # discipline = models.ManyToManyField(
    #     Discipline, verbose_name="Disciplinas", related_name="teachers"
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ["name"]


class SchoolClass(DefaultModel):
    name = models.CharField("Nome", max_length=255)

    teachers = models.ManyToManyField(
        Teacher,
        verbose_name="Professores",
        related_name="classes",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        ordering = ["name"]


class Student(DefaultModel):
    name = models.CharField("Nome", max_length=255)
    email = models.EmailField("E-mail", max_length=255)
    school_class = models.ForeignKey(
        SchoolClass, verbose_name="Turma", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        ordering = ["name"]
