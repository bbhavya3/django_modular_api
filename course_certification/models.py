from django.db import models
from course.models import Course
from certification.models import Certification


class CourseCertification(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} - {self.certification}"
