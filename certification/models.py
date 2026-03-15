from django.db import models
from course.models import Course


class Certification(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=50, unique=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name