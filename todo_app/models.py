from django.db import models
from django.contrib.auth.models import User

class Priority(models.Model):
    RED = 'R'
    GREEN = 'G'
    YELLOW = 'Y'
    COLORS = [
        (RED, 'Red'),
        (GREEN, 'Green'),
        (YELLOW, 'Yellow'),
    ]
    updated = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(
        max_length=1,
        choices = COLORS,
        default = GREEN,
    )

class Todo(models.Model):
    updated = models.DateField(auto_now_add=True)
    label = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_created=True)
    due_date = models.DateTimeField(null=True)
    completed = models.DateField()
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
    updated = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_created=True)
    start = models.DateField()
    end = models.DateField()
    all_day = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    RED = 'R'
    BLUE = 'B'
    GREEN = 'G'
    PURPLE = 'P'
    YELLOW = 'Y'
    COLORS = [
        (RED,'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (PURPLE, 'Purple'),
        (YELLOW, 'Yellow'),
    ]
    name = models.CharField(max_length=200)
    color = models.CharField(
        max_length = 1,
        choices = COLORS,
        default = RED,
    )

class TodoCategory(models.Model):
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

