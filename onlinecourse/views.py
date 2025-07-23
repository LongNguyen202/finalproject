from django.shortcuts import render
from .models import Course, Question

def course_details(request, course_id):
    course = Course.objects.get(id=course_id)
    questions = Question.objects.filter(course=course)
    return render(request, 'course_details_bootstrap.html', {
        'course': course,
        'questions': questions
    })
from .models import Submission, Question

def mock_exam_result(request):
    # Lấy submission đầu tiên (giả lập)
    submission = Submission.objects.first()
    
    if not submission:
        return render(request, 'exam_result.html', {
            'correct': 0,
            'total': 0
        })

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
