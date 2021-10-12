from django.contrib import admin

from PollsApp.models import Poll, Question, QuestionType, Choice, Vote

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Choice)
admin.site.register(Vote)
