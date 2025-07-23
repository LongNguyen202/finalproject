from django.contrib import admin
from .models import Course, Question, Choice, Submission

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
