from django.db import models
from product.models import Product
from course.models import Course

class ProductCourse(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.course}"