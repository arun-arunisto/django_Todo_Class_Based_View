from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title}'