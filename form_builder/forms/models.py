from django.db import models
from django.core.exceptions import ValidationError

class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        # Enforcing a limit of 100 questions per form
        if self.questions.count() > 100:
            raise ValidationError('A form cannot have more than 100 questions.')

    def save(self, *args, **kwargs):
        self.clean()  # Ensure clean method is called before saving
        super().save(*args, **kwargs)

class Question(models.Model):
    TEXT = 'text'
    DROPDOWN = 'dropdown'
    CHECKBOX = 'checkbox'
    
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (DROPDOWN, 'Dropdown'),
        (CHECKBOX, 'Checkbox'),
    ]
    
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    options = models.JSONField(blank=True, null=True)  # For dropdown or checkbox options
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    response = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='answers')  # Updated related_name
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    answer_choice = models.JSONField(blank=True, null=True)  # For multiple-choice options like Checkbox

    def __str__(self):
        return f"Answer {self.id} to {self.question.question_text}"

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response {self.id} for {self.form.title}"
