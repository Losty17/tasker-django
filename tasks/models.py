from django.db import models
from django.contrib.auth.models import User

from categories.models import Category


class Task(models.Model):
    PRIORITY_LOW = 0
    PRIORITY_MEDIUM = 1
    PRIORITY_HIGH = 2

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, "Low"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_HIGH, "High"),
    ]

    STATUS_PENDING = 0
    STATUS_IN_PROGRESS = 1
    STATUS_COMPLETED = 2

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)

    categories = models.ManyToManyField(
        Category, through="TaskCategories", related_name="tasks"
    )
    responsibles = models.ManyToManyField(
        User, through="TaskResponsibles", related_name="tasks"
    )

    deleted = models.BooleanField(default=False)


class TaskCategories(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.title + " - " + self.category.name


class TaskResponsibles(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.title + " - " + self.responsible.username
