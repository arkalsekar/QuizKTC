# Generated by Django 4.2.4 on 2024-08-05 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_questions_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='answerfor', to='home.quiz'),
            preserve_default=False,
        ),
    ]