from django.contrib import admin
from api.models import Workout, Exercise, Progress, Goal

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]
    list_display = ['name', 'date', 'user']

class ProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'height', 'body_fat_percentage', 'bmi', 'date']

class GoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'goal_type', 'target', 'start_date', 'end_date']

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Exercise)