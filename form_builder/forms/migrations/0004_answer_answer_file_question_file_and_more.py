# Generated by Django 5.1.4 on 2025-01-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_alter_answer_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_file',
            field=models.FileField(blank=True, null=True, upload_to='answers/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox'), ('file', 'File')], max_length=20),
        ),
    ]
