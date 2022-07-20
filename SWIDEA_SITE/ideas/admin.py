from django.contrib import admin
from .models import Idea, Tool

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass
