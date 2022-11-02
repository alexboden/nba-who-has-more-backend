from django.contrib import admin

from .models import Question, Player

admin.site.register(Question)
admin.site.register(Player)