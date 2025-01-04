# Generated by Django 5.1.4 on 2025-01-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_answer_answer_file_question_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_file',
        ),
        migrations.RemoveField(
            model_name='question',
            name='file',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox')], max_length=20),
        ),
    ]