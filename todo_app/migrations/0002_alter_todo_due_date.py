# Generated by Django 4.0.4 on 2022-04-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
