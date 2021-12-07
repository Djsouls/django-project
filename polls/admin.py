from django.contrib import admin

from .models import Question, Choice

# Making models accessable via admin page
admin.site.register(Question)
admin.site.register(Choice)
