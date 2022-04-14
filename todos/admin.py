from django.contrib import admin
from .models import Priority, Todo, Event, Category, TodoCategory

admin.site.register(Priority)
admin.site.register(Todo)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(TodoCategory)