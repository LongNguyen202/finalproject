from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

from .models import Submission, Choice

def mock_exam_result(request):
    # Giả lập lấy dữ liệu từ submission (trong thực tế sẽ nhận từ form POST)
    submission = Submission.objects.first()  # lấy submission đầu tiên
    selected_choices = submission.choices.all()
    
    total_questions = Question.objects.count()
    correct_answers = 0

    for question in Question.objects.all():
        correct_choices = set(question.choice_set.filter(is_correct=True))
        selected_for_question = set(selected_choices.filter(question=question))
        if correct_choices == selected_for_question:
            correct_answers += 1

    return render(request, 'exam_result.html', {
        'correct': correct_answers,
        'total': total_questions
    })
