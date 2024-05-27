from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.date}'


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.workout}'


class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()

    @property
    def bmi(self):
        if self.weight and self.height:
            height_in_meters = self.height / 100
            return self.weight / (height_in_meters ** 2)
        return None

    def __str__(self):
        return f'{self.user} - {self.date}'



class Goal(models.Model):
    GOAL_TYPE_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('body_fat_percentage_reduction', 'Body Fat Percentage Reduction'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance_improvement', 'Endurance Improvement'),
        ('strength_improvement', 'Strength Improvement'),
        ('distance_running', 'Distance Running'),
        ('distance_cycling', 'Distance Cycling'),
        ('distance_swimming', 'Distance Swimming'),
        ('number_of_workouts_per_week', 'Number of Workouts per Week'),
        ('number_of_steps_per_day', 'Number of Steps per Day'),
        ('calorie_intake_reduction', 'Calorie Intake Reduction'),
        ('calorie_intake_increase', 'Calorie Intake Increase'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=255, choices=GOAL_TYPE_CHOICES)
    target = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.user} - {self.get_goal_type_display()}'