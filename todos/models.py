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
    priority = models.CharField(max_length=50, blank=True)
    color = models.CharField(
        max_length=1,
        choices=COLORS,
        default=GREEN,
    )

    class Meta:
        verbose_name_plural = 'Priorities'
        
    def __str__(self):
        return self.color


class Todo(models.Model):
    updated = models.DateField(auto_now_add=True)
    label = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_created=True)
    due_date = models.DateTimeField(blank=True)
    completed = models.DateField(null=True,blank=True)
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Event(models.Model):
    updated = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_created=True)
    start = models.DateField(blank=True)
    end = models.DateField(blank=True)
    all_day = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    RED = 'R'
    BLUE = 'B'
    GREEN = 'G'
    PURPLE = 'P'
    YELLOW = 'Y'
    COLORS = [
        (RED, 'Red'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (PURPLE, 'Purple'),
        (YELLOW, 'Yellow'),
    ]
    name = models.CharField(max_length=200)
    color = models.CharField(
        max_length=1,
        choices=COLORS,
        default=RED,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class TodoCategory(models.Model):
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo_category_text