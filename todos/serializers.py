from .models import Todo, Event, Category
from rest_framework import serializers
      
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class PrioritySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Priority
#         fields = [
#             '__all__',
#         ]

# class TodoCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = TodoCategory
#         fields = [
#             'url',
#             'todo_id',
#             'category_id',
#         ]