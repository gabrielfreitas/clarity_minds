# Generated by Django 4.2.5 on 2023-10-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0002_alter_feedback_emoji"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="is_anonymous",
            field=models.BooleanField(default=True, verbose_name="Anônimo"),
        ),
    ]
